from collections import namedtuple

from colors import RED, GREEN, BLUE, WHITE, BLACK, color_to_string

ImmutableCard = namedtuple("Card",
        ["id", "points", "color", "cost"])

def create_card(id, points, color, total_cost,
    red_cost, green_cost, blue_cost, white_cost, black_cost):
    """total_cost is for debugging. This is using immutable cards.
    Using immutable cards is far slower."""
    # error-checking
    cost_dict = {
        RED: red_cost,
        GREEN: green_cost,
        BLUE: blue_cost,
        WHITE: white_cost,
        BLACK: black_cost
    }
    try:
        assert(cost_dict[RED] + cost_dict[GREEN] + cost_dict[BLUE] +
                cost_dict[WHITE] + cost_dict[BLACK] == total_cost)
    except AssertionError as e:
        print("Cost error check failed for card %s" % repr(self))
        raise e
    return ImmutableCard(
        id = id,
        cost = cost_dict,
        points = points,
        color = color
    )


class Card(object):
    def __init__(self, id, total_cost, points, color, level,
            red_cost, green_cost, blue_cost, white_cost, black_cost):
        """total_cost is for debugging"""
        self.id = id
        self.cost = {
            RED: red_cost,
            GREEN: green_cost,
            BLUE: blue_cost,
            WHITE: white_cost,
            BLACK: black_cost
        }
        self.points = points
        self.color = color
        self.level = level

        # error-checking
        try:
            assert(self.cost[RED] + self.cost[GREEN] + self.cost[BLUE] +
                    self.cost[WHITE] + self.cost[BLACK] == total_cost)
        except AssertionError as e:
            print("Cost error check failed for card %s" % repr(self))
            raise e

    def cost_string(self):
        return "{%s}" %\
                ", ".join(["{}: {}".format(color_to_string(color), cost)
                    for color, cost in self.cost.items()])

    def __repr__(self):
        return str(self.__dict__)

    def __str__(self):
        return "Card (id={}, color={}, cost={}, points={})".format(
                self.id, color_to_string(self.color),
                self.cost_string(), self.points)

card_list = [
    # Level 1
    # card type 1
    Card(id=1, color=RED, total_cost=4,  points=0, level=1,
        red_cost=0, green_cost=1, blue_cost=1, white_cost=1, black_cost=1),
    Card(id=2, color=GREEN, total_cost=4, points=0, level=1,
        red_cost=1, green_cost=0, blue_cost=1, white_cost=1, black_cost=1),
    Card(id=3, color=BLUE, total_cost=4, points=0, level=1,
        red_cost=1, green_cost=1, blue_cost=0, white_cost=1, black_cost=1),
    Card(id=4, color=WHITE, total_cost=4, points=0, level=1,
        red_cost=1, green_cost=1, blue_cost=1, white_cost=0, black_cost=1),
    Card(id=5, color=BLACK, total_cost=4, points=0, level=1,
        red_cost=1, green_cost=1, blue_cost=1, white_cost=1, black_cost=0),

    # card type 2
    Card(id=6, color=RED, total_cost=5, points=0, level=1,
        red_cost=0, green_cost=1, blue_cost=1, white_cost=2, black_cost=1),
    Card(id=7, color=GREEN, total_cost=5, points=0, level=1,
        red_cost=1, green_cost=0, blue_cost=1, white_cost=1, black_cost=2),
    Card(id=8, color=BLUE, total_cost=5, points=0, level=1,
        red_cost=2, green_cost=1, blue_cost=0, white_cost=1, black_cost=1),
    Card(id=9, color=WHITE, total_cost=5, points=0, level=1,
        red_cost=1, green_cost=2, blue_cost=1, white_cost=0, black_cost=1),
    Card(id=10, color=BLACK, total_cost=5, points=0, level=1,
        red_cost=1, green_cost=1, blue_cost=2, white_cost=1, black_cost=0),

    # card type 3
    Card(id=11, color=BLACK, total_cost=5, points=0, level=1,
        white_cost=2, blue_cost=2, green_cost=0, red_cost=1, black_cost=0),
    Card(id=12, color=BLUE, total_cost=5, points=0, level=1,
        white_cost=1, blue_cost=0, green_cost=2, red_cost=2, black_cost=0),
    Card(id=13, color=WHITE, total_cost=5, points=0, level=1,
        white_cost=0, blue_cost=2, green_cost=2, red_cost=0, black_cost=1),
    Card(id=14, color=GREEN, total_cost=5, points=0, level=1,
        white_cost=0, blue_cost=1, green_cost=0, red_cost=2, black_cost=2),
    Card(id=15, color=RED, total_cost=5, points=0, level=1,
        white_cost=2, blue_cost=0, green_cost=1, red_cost=0, black_cost=2),

    # card type 4
    Card(id=16, color=BLACK, total_cost=5, points=0, level=1,
        white_cost=0, blue_cost=0, green_cost=1, red_cost=3, black_cost=1),
    Card(id=17, color=BLUE, total_cost=5, points=0, level=1,
        white_cost=0, blue_cost=1, green_cost=3, red_cost=1, black_cost=0),
    Card(id=18, color=WHITE, total_cost=5, points=0, level=1,
        white_cost=3, blue_cost=1, green_cost=0, red_cost=0, black_cost=1),
    Card(id=19, color=GREEN, total_cost=5, points=0, level=1,
        white_cost=1, blue_cost=3, green_cost=1, red_cost=0, black_cost=0),
    Card(id=20, color=RED, total_cost=5, points=0, level=1,
        white_cost=1, blue_cost=0, green_cost=0, red_cost=1, black_cost=3),

    # card type 5
    Card(id=21, color=BLACK, total_cost=3, points=0, level=1,
        white_cost=0, blue_cost=0, green_cost=2, red_cost=1, black_cost=0),
    Card(id=22, color=BLUE, total_cost=3, points=0, level=1,
        white_cost=1, blue_cost=0, green_cost=0, red_cost=0, black_cost=2),
    Card(id=23, color=WHITE, total_cost=3, points=0, level=1,
        white_cost=0, blue_cost=0, green_cost=0, red_cost=2, black_cost=1),
    Card(id=24, color=GREEN, total_cost=3, points=0, level=1,
        white_cost=2, blue_cost=1, green_cost=0, red_cost=0, black_cost=0),
    Card(id=25, color=RED, total_cost=3, points=0, level=1,
        white_cost=0, blue_cost=2, green_cost=1, red_cost=0, black_cost=0),

    # card type 6
    Card(id=26, color=BLACK, total_cost=4, points=0, level=1,
        white_cost=2, blue_cost=0, green_cost=2, red_cost=0, black_cost=0),
    Card(id=27, color=BLUE, total_cost=4, points=0, level=1,
        white_cost=0, blue_cost=0, green_cost=2, red_cost=0, black_cost=2),
    Card(id=28, color=WHITE, total_cost=4, points=0, level=1,
        white_cost=0, blue_cost=2, green_cost=0, red_cost=0, black_cost=2),
    Card(id=29, color=GREEN, total_cost=4, points=0, level=1,
        white_cost=0, blue_cost=2, green_cost=0, red_cost=2, black_cost=0),
    Card(id=30, color=RED, total_cost=4, points=0, level=1,
        white_cost=2, blue_cost=0, green_cost=0, red_cost=2, black_cost=0),

    # card type 7
    Card(id=31, color=RED, total_cost=3, points=0, level=1,
        red_cost=0, green_cost=0, blue_cost=0, white_cost=3, black_cost=0),
    Card(id=32, color=GREEN, total_cost=3, points=0, level=1,
        red_cost=3, green_cost=0, blue_cost=0, white_cost=0, black_cost=0),
    Card(id=33, color=BLUE, total_cost=3, points=0, level=1,
        red_cost=0, green_cost=0, blue_cost=0, white_cost=0, black_cost=3),
    Card(id=34, color=WHITE, total_cost=3, points=0, level=1,
        red_cost=0, green_cost=0, blue_cost=3, white_cost=0, black_cost=0),
    Card(id=35, color=BLACK, total_cost=3, points=0, level=1,
        red_cost=0, green_cost=3, blue_cost=0, white_cost=0, black_cost=0),

    # card type 8
    Card(id=36, color=BLACK, total_cost=4, points=1, level=1,
        white_cost=0, blue_cost=4, green_cost=0, red_cost=0, black_cost=0),
    Card(id=37, color=BLUE, total_cost=4, points=1, level=1,
        white_cost=0, blue_cost=0, green_cost=0, red_cost=4, black_cost=0),
    Card(id=38, color=WHITE, total_cost=4, points=1, level=1,
        white_cost=0, blue_cost=0, green_cost=4, red_cost=0, black_cost=0),
    Card(id=39, color=GREEN, total_cost=4, points=1, level=1,
        white_cost=0, blue_cost=0, green_cost=0, red_cost=0, black_cost=4),
    Card(id=40, color=RED, total_cost=4, points=1, level=1,
        white_cost=4, blue_cost=0, green_cost=0, red_cost=0, black_cost=0),

    # Level 2

    # card type 9
    Card(id=101, color=RED, total_cost=7, points=1, level=2,
        red_cost=2, green_cost=0, blue_cost=0, white_cost=2, black_cost=3),
    # green has type 1 and 2 reversed in table (for level 2)
    Card(id=102, color=GREEN, total_cost=7, points=1, level=2,
        red_cost=0, green_cost=0, blue_cost=3, white_cost=2, black_cost=2),
    Card(id=103, color=BLUE, total_cost=7, points=1, level=2,
        red_cost=3, green_cost=2, blue_cost=2, white_cost=0, black_cost=0),
    Card(id=104, color=WHITE, total_cost=7, points=1, level=2,
        red_cost=2, green_cost=3, blue_cost=0, white_cost=0, black_cost=2),
    Card(id=105, color=BLACK, total_cost=7, points=1, level=2,
        red_cost=0, green_cost=2, blue_cost=2, white_cost=3, black_cost=0),

    # card type 10
    Card(id=106, color=BLACK, total_cost=8, points=1, level=2,
        white_cost=3, blue_cost=0, green_cost=3, red_cost=0, black_cost=2),
    Card(id=107, color=BLUE, total_cost=8, points=1, level=2,
        white_cost=0, blue_cost=2, green_cost=3, red_cost=0, black_cost=3),
    Card(id=108, color=WHITE, total_cost=8, points=1, level=2,
        white_cost=2, blue_cost=3, green_cost=0, red_cost=3, black_cost=0),
    Card(id=109, color=GREEN, total_cost=8, points=1, level=2,
        white_cost=3, blue_cost=0, green_cost=2, red_cost=3, black_cost=0),
    Card(id=110, color=RED, total_cost=8, points=1, level=2,
        white_cost=0, blue_cost=3, green_cost=0, red_cost=2, black_cost=3),

    # card type 11
    Card(id=111, color=BLACK, total_cost=7, points=2, level=2,
        white_cost=0, blue_cost=1, green_cost=4, red_cost=2, black_cost=0),
    # 3 and 4 are backwards for blue
    Card(id=112, color=BLUE, total_cost=7, points=2, level=2,
        white_cost=2, blue_cost=0, green_cost=0, red_cost=1, black_cost=4),
    Card(id=113, color=WHITE, total_cost=7, points=2, level=2,
        white_cost=0, blue_cost=0, green_cost=1, red_cost=4, black_cost=2),
    Card(id=114, color=GREEN, total_cost=7, points=2, level=2,
        white_cost=4, blue_cost=2, green_cost=0, red_cost=0, black_cost=1),
    Card(id=115, color=RED, total_cost=7, points=2, level=2,
        white_cost=1, blue_cost=4, green_cost=2, red_cost=0, black_cost=0),

    # card type 12
    Card(id=116, color=BLACK, total_cost=8, points=2, level=2,
        white_cost=0, blue_cost=0, green_cost=5, red_cost=3, black_cost=0),
    # 3 and 4 are backwards for blue
    Card(id=117, color=BLUE, total_cost=8, points=2, level=2,
        white_cost=5, blue_cost=3, green_cost=0, red_cost=0, black_cost=0),
    Card(id=118, color=WHITE, total_cost=8, points=2, level=2,
        white_cost=0, blue_cost=0, green_cost=0, red_cost=5, black_cost=3),
    Card(id=119, color=GREEN, total_cost=8, points=2, level=2,
        white_cost=0, blue_cost=5, green_cost=3, red_cost=0, black_cost=0),
    Card(id=120, color=RED, total_cost=8, points=2, level=2,
        white_cost=3, blue_cost=0, green_cost=0, red_cost=0, black_cost=5),

    # card type 13
    Card(id=121, color=BLACK, total_cost=5, points=2, level=2,
        white_cost=5, blue_cost=0, green_cost=0, red_cost=0, black_cost=0),
    Card(id=122, color=BLUE, total_cost=5, points=2, level=2,
        white_cost=0, blue_cost=5, green_cost=0, red_cost=0, black_cost=0),
    Card(id=123, color=WHITE, total_cost=5, points=2, level=2,
        white_cost=0, blue_cost=0, green_cost=0, red_cost=5, black_cost=0),
    Card(id=124, color=GREEN, total_cost=5, points=2, level=2,
        white_cost=0, blue_cost=0, green_cost=5, red_cost=0, black_cost=0),
    Card(id=125, color=RED, total_cost=5, points=2, level=2,
        white_cost=0, blue_cost=0, green_cost=0, red_cost=0, black_cost=5),

    # card type 14
    Card(id=126, color=BLACK, total_cost=6, points=3, level=2,
        white_cost=0, blue_cost=0, green_cost=0, red_cost=0, black_cost=6),
    Card(id=127, color=BLUE, total_cost=6, points=3, level=2,
        white_cost=0, blue_cost=6, green_cost=0, red_cost=0, black_cost=0),
    Card(id=128, color=WHITE, total_cost=6, points=3, level=2,
        white_cost=6, blue_cost=0, green_cost=0, red_cost=0, black_cost=0),
    Card(id=129, color=GREEN, total_cost=6, points=3, level=2,
        white_cost=0, blue_cost=0, green_cost=6, red_cost=0, black_cost=0),
    Card(id=130, color=RED, total_cost=6, points=3, level=2,
        white_cost=0, blue_cost=0, green_cost=0, red_cost=6, black_cost=0),

    # Level 3

    # card type 15
    Card(id=201, color=RED, total_cost=14, points=3, level=3,
        red_cost=0, green_cost=3, blue_cost=5, white_cost=3, black_cost=3),
    Card(id=202, color=GREEN, total_cost=14, points=3, level=3,
        red_cost=3, green_cost=0, blue_cost=3, white_cost=5, black_cost=3),
    Card(id=203, color=BLUE, total_cost=14, points=3, level=3,
        red_cost=3, green_cost=3, blue_cost=0, white_cost=3, black_cost=5),
    Card(id=204, color=WHITE, total_cost=14, points=3, level=3,
        red_cost=5, green_cost=3, blue_cost=3, white_cost=0, black_cost=3),
    Card(id=205, color=BLACK, total_cost=14, points=3, level=3,
        red_cost=3, green_cost=5, blue_cost=3, white_cost=3, black_cost=0),

    # card type 16
    Card(id=206, color=RED, total_cost=7, points=4, level=3,
        red_cost=0, green_cost=7, blue_cost=0, white_cost=0, black_cost=0),
    Card(id=207, color=GREEN, total_cost=7, points=4, level=3,
        red_cost=0, green_cost=0, blue_cost=7, white_cost=0, black_cost=0),
    Card(id=208, color=BLUE, total_cost=7, points=4, level=3,
        red_cost=0, green_cost=0, blue_cost=0, white_cost=7, black_cost=0),
    Card(id=209, color=WHITE, total_cost=7, points=4, level=3,
        red_cost=0, green_cost=0, blue_cost=0, white_cost=0, black_cost=7),
    Card(id=210, color=BLACK, total_cost=7, points=4, level=3,
        red_cost=7, green_cost=0, blue_cost=0, white_cost=0, black_cost=0),

    # card type 17
    Card(id=211, color=RED, total_cost=12, points=0, level=3,
        red_cost=3, green_cost=6, blue_cost=3, white_cost=0, black_cost=0),
    Card(id=212, color=GREEN, total_cost=12, points=0, level=3,
        red_cost=0, green_cost=3, blue_cost=6, white_cost=3, black_cost=0),
    Card(id=213, color=BLUE, total_cost=12, points=0, level=3,
        red_cost=0, green_cost=0, blue_cost=3, white_cost=6, black_cost=3),
    Card(id=214, color=WHITE, total_cost=12, points=0, level=3,
        red_cost=3, green_cost=0, blue_cost=0, white_cost=3, black_cost=6),
    Card(id=215, color=BLACK, total_cost=12, points=0, level=3,
        red_cost=6, green_cost=3, blue_cost=0, white_cost=0, black_cost=3),

    # card type 18
    Card(id=216, color=RED, total_cost=10, points=5, level=3,
        red_cost=3, green_cost=7, blue_cost=0, white_cost=0, black_cost=0),
    Card(id=217, color=GREEN, total_cost=10, points=5, level=3,
        red_cost=0, green_cost=3, blue_cost=7, white_cost=0, black_cost=0),
    Card(id=218, color=BLUE, total_cost=10, points=5, level=3,
        red_cost=0, green_cost=0, blue_cost=3, white_cost=7, black_cost=0),
    Card(id=219, color=WHITE, total_cost=10, points=5, level=3,
        red_cost=0, green_cost=0, blue_cost=0, white_cost=3, black_cost=7),
    Card(id=220, color=BLACK, total_cost=10, points=5, level=3,
        red_cost=7, green_cost=0, blue_cost=0, white_cost=0, black_cost=3),
]
for idx, card in enumerate(card_list):
    card.index = idx
