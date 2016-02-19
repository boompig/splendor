from __future__ import print_function
from cards import card_list
import copy
from queue import PriorityQueue
import time
from collections import deque


class State:
    def __init__(self, money, points, turn):
        self.money = money
        self.points = points
        self.turn = turn
        self.num_cards = 0
        self.cards = []

    def __hash__(self):
        # sum of all the different things
        # points are always < 100
        # money is always <= 10, so < 100
        return self.money + (self.points * 100) + (self.turn * 100 * 100)


def can_take_money(current_state):
    return current_state.money <= 7

def change_state_take_money(current_state):
    """Return new state resulting in taking money in the current state.
    Assume can take money. Do not modify current state"""
    # given that can take money
    new_state = copy.deepcopy(current_state)
    new_state.money += 3
    new_state.turn += 1
    return new_state

def can_afford_card(current_state, card):
    return current_state.money >= card.cost

def change_state_buy_card(current_state, card):
    """Return new state resulting in buying the given card from the given state
    Assume that this is a legal action. Do not alter given state"""
    # given that can afford card in current state
    new_state = copy.deepcopy(current_state)
    new_state.num_cards += 1
    new_state.money -= card.cost
    new_state.points += card.points
    new_state.turn += 1
    new_state.cards.append(card)
    return new_state

def get_successor_states(current_state):
    """Generator over successor states"""
    if can_take_money(current_state):
        s1 = change_state_take_money(current_state)
        yield s1
    for card in card_list:
        if can_afford_card(current_state, card):
            s = change_state_buy_card(current_state, card)
            yield s

def is_goal_state(state):
    return state.points >= 15

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
    return (None, num_states)

def bfs_with_visited(starting_state):
    visited = set([])
    num_states = 0
    if is_goal_state(starting_state):
        num_states += 1
        return (starting_state, num_states)
    h = hash(starting_state)
    #print("Adding %d to visited" % h)
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
                h = hash(next_state)
                if h not in visited:
                    #print("Adding %d to visited" % h)
                    visited.add(h)
                    open_list.append(next_state)
    return (None, num_states)


def search():
    starting_state = State(money=0, points=0, turn=0)
    
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
        print("Won with the following cards")
        for idx, card in enumerate(final_state.cards):
            print("%d. %s" % (idx + 1, str(card)))
    else:
        print("Did not find goal state")


if __name__ == "__main__":
    search()
