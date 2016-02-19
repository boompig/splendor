import copy
# command line

cheap_card = {
    "cost": 4,
    "points": 1
}

medium_card = {
    "cost": 7,
    "points": 2
}

pricy_card = {
    "cost": 12,
    "points": 5
}

class Player(object):
    def __init__(self):
        self.cards = {
            "cheap": 0,
            "medium": 0,
            "pricy": 0
        }
        self.points = 0
        self.money = 0

    def take_money(self):
        try :
            assert(self.money <= 7)
            self.money += 3
            return True
        except AssertionError:
            print "too much money!"
            return False

    def buy_card(self, type):
        if type == "cheap":
            card = cheap_card
        elif type == "medium":
            card = medium_card
        elif type == "pricy":
            card = pricy_card
        else:
            print "error: invalid type: %s" % type
            return
        try:
            assert(self.money >= card["cost"])
        except AssertionError:
            print "error: cannot afford"
            return
        self.cards[type] += 1
        self.points += card["points"]
        self.money -= card["cost"]

    def can_buy_card(self, type):
        if type == "cheap":
            card = cheap_card
        elif type == "medium":
            card = medium_card
        elif type == "pricy":
            card = pricy_card
        else:
            print "error: invalid type: %s" % type
            return False
        return self.money >= card["cost"]

    def print_cards(self):
        for card_type, amt in self.cards.iteritems():
            print "%s -> %d" % (card_type, amt)


def buy_card(player, card_type):
    if card_type in player.cards:
        if player.can_buy_card(card_type):
            player.buy_card(card_type)
            player.print_cards()
            print "points now at %d" % player.points
            print "money now at %d" % player.money
            return True
        else:
            print "Error: cannot afford card type %s" % card_type
            return False
    else:
        return False

def take_money(player):
    success = player.take_money()
    print "money now at %d" % player.money
    return success

if __name__ == "__main__":
    player = Player()
    finished = False
    turn = 1
    while (not finished) and player.points < 15:
        user_input = raw_input("[turn %d] command> " % turn)
        if user_input == "money":
            success = take_money(player)
            if success:
                turn += 1
        elif user_input.split(" ")[0] == "card":
            try:
                card_type = user_input.split(" ")[1]
            except IndexError:
                print "Error: card type not specified"
                continue
            try:
                assert(card_type in player.cards)
                success = buy_card(player, card_type)
                if success:
                    turn += 1
            except AssertionError:
                print "Error: unrecognized card type: %s" % card_type
                print "Valid types: %s" % ", ".join([k for k in player.cards])
                continue
        elif user_input == "quit" or user_input == "exit":
            finished = True
        else:
            print "Error: unknown command: %s" % user_input
    if player.points >= 15:
        print "Game over, player won"
    else:
        print "Goodbye"
