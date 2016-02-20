from __future__ import print_function
import copy
from queue import PriorityQueue
import time
from collections import deque, namedtuple
import pdb
import itertools

from cards import card_list, RED, GREEN, BLUE, WHITE, BLACK
from nobles import noble_list

"""
Simplifying assumptions:
    * no ability to reserve cards

    * some cards missing
    * some nobles missing
"""

# options for search:
search_options = {
    "immutable_state": False,
    "print_progress": True,
    "progress_granularity": 100000
}

def get_money_permutations():
    all_colors = [RED, GREEN, BLUE, WHITE, BLACK]
    for color_list in itertools.combinations(all_colors, 3):
        d = {}
        for color in color_list:
            d[color] = 1
        yield d
    for color in all_colors:
        d = { color: 2 }
        yield d

# these are static so don't have to compute them every time
money_permutations = list(get_money_permutations())

# immutable object!
ImmutableState = namedtuple("ImmutableState",
        ["money", "points", "turn", "cards", "nobles"])

def hash_state(state):
    if search_options["immutable_state"]:
        card_hash = str(sorted(state.cards))
        money_hash = str(sorted(state.money.items()))
        # I wonder if this is entirely legit...
        #card_hash = hash(state.cards)
        #nobles_hash = hash(state.nobles)
        #t = (state.money, state.points, state.turn, card_hash, nobles_hash)
        t = (money_hash, state.points, state.turn, card_hash)
        return hash(t)
    else:
        card_hash = tuple(sorted(state.cards))
        money_hash = tuple(sorted(state.money.items()))
        t = (money_hash, state.points, state.turn, card_hash)
        return hash(t)

def get_color_distribution(card_set):
    """Return current color distribution of cards"""
    color_distribution = {
        RED: 0,
        GREEN: 0,
        BLUE: 0,
        WHITE: 0,
        BLACK: 0
    }
    for card_id in card_set:
        card = card_list[card_id]
        color_distribution[card.color] += 1
    return color_distribution

def check_nobles(card_set, noble_set):
    """Add all nobles which apply to noble set. Return resulting point bonus"""
    points_bonus = 0
    color_distribution = get_color_distribution(card_set)
    for idx, noble in enumerate(noble_list):
        if noble.noble_applies(color_distribution):
            if idx not in noble_set:
                noble_set.add(idx)
                points_bonus += noble.points
    return points_bonus

def has_card(state, card, card_index):
    return card_index in state.cards

def get_card_cost(state, target_card):
    cost = copy.copy(target_card.cost)
    for card_index in state.cards:
        card = card_list[card_index]
        cost[card.color] = max(0, cost[card.color] - 1)
    return cost

class State:
    __slots__ = ["points", "turn", "money", "cards", "nobles"]
    def __init__(self, points: int, turn: int, cards, nobles, money):
        # map from color to amt
        self.money = money

        self.points = points
        self.turn = turn

        # indices of cards
        self.cards = cards

        # indices of nobles
        # we don't need to explicitly keep track of these here
        # because cards determine nobles
        self.nobles = nobles


def print_cards(state):
    for idx, card_index in enumerate(state.cards):
        card = card_list[card_index]
        print("%d. %s" % (idx + 1, str(card)))

def print_nobles(state):
    if len(state.nobles) == 0:
        print("No nobles")
    for idx, noble_index in enumerate(state.nobles):
        noble = noble_list[noble_index]
        print("%d. %s" % (idx + 1, str(noble)))

def count_money(current_state):
    return sum([amt for color, amt in current_state.money.items()])

def can_take_money(current_state):
    return count_money(current_state) <= 7

def apply_money_diff(money_dict, diff):
    for color in money_dict:
        if color in diff:
            money_dict[color] += diff[color]

def change_state_take_money(current_state, money_diff):
    """Return new state resulting in taking money in the current state.
    Assume can take money. Do not modify current state"""
    new_money_dict = copy.copy(current_state.money)
    apply_money_diff(new_money_dict, money_diff)
    if search_options["immutable_state"]:
        new_state = ImmutableState(
            money=new_money_dict,
            points=current_state.points,
            turn=current_state.turn + 1,
            cards=current_state.cards,
            nobles=current_state.nobles
        )
    else:
        # no need to copy lists/sets because they are not modified
        new_state = State(
            money=new_money_dict,
            points=current_state.points,
            turn=current_state.turn + 1,
            cards=current_state.cards,
            nobles=current_state.nobles
        )
    return new_state

def can_afford_card(current_state, card):
    card_cost = get_card_cost(current_state, card)
    for color in current_state.money:
        if current_state.money[color] < card_cost[color]:
            return False
    return True

def absolute_card_cost(card_cost):
    return sum([amt for color, amt in card_cost.items()])

def deduct_cost(money_dict, card_cost_dict):
    for color in card_cost_dict:
        money_dict[color] -= card_cost_dict[color]

def change_state_buy_card_immutable(current_state, card, card_index):
    # mapping from color to cost, taking into account discounts
    card_cost = get_card_cost(current_state, card)
    points_bonus = card.points
    # no need to do crazy copy, this was just a frozenset of ints before
    new_cards = set(current_state.cards)
    # no need to do crazy copy, this was just a frozenset of ints before
    new_nobles = set(current_state.nobles)
    new_money_dict = copy.copy(current_state.money)
    new_cards.append(card_index)
    deduct_cost(new_money_dict, card_cost)
    # also adds nobles to nobles set
    if len(new_cards) >= 8:
        # only check nobles conditionally, because it is a slow op
        points_bonus += check_nobles(new_cards, new_nobles)
    new_state = ImmutableState(
        money = new_money_dict,
        points = current_state.points + points_bonus,
        turn = current_state.turn + 1,
        cards = frozenset(new_cards),
        nobles = frozenset(new_nobles)
    )
    return new_state

def change_state_buy_card_mutable(current_state, card, card_index):
    # mapping from color to cost, taking into account discounts
    card_cost = get_card_cost(current_state, card)
    points_bonus = card.points
    # copy container
    new_cards = copy.copy(current_state.cards)
    # copy container
    new_nobles = copy.copy(current_state.nobles)
    # copy dict
    new_money_dict = copy.copy(current_state.money)
    new_cards.append(card_index)
    deduct_cost(new_money_dict, card_cost)
    # also adds nobles to nobles set
    if len(new_cards) >= 8:
        # only check nobles conditionally, because it is a slow op
        points_bonus += check_nobles(new_cards, new_nobles)
    new_state = State(
        money = new_money_dict,
        points = current_state.points + points_bonus,
        turn = current_state.turn + 1,
        cards = new_cards,
        nobles = new_nobles
    )
    return new_state

def change_state_buy_card(current_state, card, card_index):
    """Return new state resulting in buying the given card from the given state
    Assume that this is a legal action. Do not alter given state"""
    if search_options["immutable_state"]:
        return change_state_buy_card_immutable(current_state, card, card_index)
    else:
        return change_state_buy_card_mutable(current_state, card, card_index)

def can_buy_card(current_state, card, card_index):
    return (can_afford_card(current_state, card) and\
            not has_card(current_state, card, card_index))

def get_successor_states(current_state):
    """Generator over successor states"""
    if can_take_money(current_state):
        for money_diff in money_permutations:
            s = change_state_take_money(current_state, money_diff)
            yield s
    for card_index, card in enumerate(card_list):
        if can_buy_card(current_state, card, card_index):
            s = change_state_buy_card(current_state, card, card_index)
            yield s

def is_goal_state(state):
    return state.points >= 6

def bfs(starting_state):
    """Given starting state, conduct BFS until find the goal state.
    Return the goal state and the level at which it was found.
    Level numbering is 0 for starting state, +1 for successors"""
    num_states = 0
    if is_goal_state(starting_state):
        num_states += 1
        return (starting_state, num_states)
    open_list = deque([starting_state])
    while len(open_list) > 0:
        state = open_list.popleft()
        # we know it's not a goal because was checked before
        for next_state in get_successor_states(state):
            num_states += 1
            if is_goal_state(next_state):
                return (next_state, num_states)
            else:
                open_list.append(next_state)
            if(search_options["print_progress"] and\
                    num_states % search_options["progress_granularity"] == 0):
                print("Number of expanded states=%d" % num_states)
    return (None, num_states)

def bfs_with_visited(starting_state):
    visited = set([])
    num_states = 0
    if is_goal_state(starting_state):
        num_states += 1
        return (starting_state, num_states)
    h = hash_state(starting_state)
    visited.add(h)
    open_list = deque([starting_state])
    while len(open_list) > 0:
        state = open_list.popleft()
        # we know it's not a goal because was checked before
        for next_state in get_successor_states(state):
            num_states += 1
            if is_goal_state(next_state):
                return (next_state, num_states)
            else:
                h = hash_state(next_state)
                if h not in visited:
                    visited.add(h)
                    open_list.append(next_state)
            if(search_options["print_progress"] and\
                    num_states % search_options["progress_granularity"] == 0):
                print("Number of expanded states=%d" % num_states)
    return (None, num_states)

def search():
    search_options["immutable_state"] = False
    search_options["print_progress"] = True

    starting_money = {
        RED: 0,
        GREEN: 0,
        BLUE: 0,
        WHITE: 0,
        BLACK: 0
    }
    if search_options["immutable_state"]:
        starting_state = ImmutableState(
            money=starting_money, points=0, turn=0,
            cards=frozenset([]), nobles=frozenset([])
        )
    else:
        starting_state = State(money=starting_money, points=0, turn=0,
                cards=[], nobles=[])

    # BFS
    #search_algo_name = "pure BFS"
    #search_algo = bfs

    # BFS with visited
    search_algo_name = "BFS with visited set"
    search_algo = bfs_with_visited

    print("starting search with algorithm '%s'..." % search_algo_name)
    start_time = time.time()
    final_state, num_states = search_algo(starting_state)
    elapsed_time = time.time() - start_time

    print("Elapsed time = %.2f seconds" % elapsed_time)
    print("Examined %d states" % num_states)

    if final_state:
        print("Found optimal strategy which takes %d turns" % final_state.turn)
        print("Won with the following cards:")
        print_cards(final_state)
        print("Won with the following nobles:")
        print_nobles(final_state)
    else:
        print("Did not find goal state")


if __name__ == "__main__":
    search()
