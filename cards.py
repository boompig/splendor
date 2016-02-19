from colors import RED, GREEN, BLUE, WHITE, BLACK, color_to_string

class Card(object):
    def __init__(self, id, total_cost, points, color,
            red_cost, green_cost, blue_cost, white_cost,
            black_cost):
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

# there are different distributions for gems
card_list = [
    # Level 1
    # card type 1
    Card(id=1, color=RED, total_cost=4,  points=0,
        red_cost=0, green_cost=1, blue_cost=1, white_cost=1, black_cost=1),
    Card(id=2, color=GREEN, total_cost=4, points=0,
        red_cost=1, green_cost=0, blue_cost=1, white_cost=1, black_cost=1),
    Card(id=3, color=BLUE, total_cost=4, points=0,
        red_cost=1, green_cost=1, blue_cost=0, white_cost=1, black_cost=1),
    Card(id=4, color=WHITE, total_cost=4, points=0,
        red_cost=1, green_cost=1, blue_cost=1, white_cost=0, black_cost=1),
    Card(id=5, color=BLACK, total_cost=4, points=0,
        red_cost=1, green_cost=1, blue_cost=1, white_cost=1, black_cost=0),

    # card type 2
    Card(id=6, color=RED, total_cost=5, points=0,
        red_cost=0, green_cost=1, blue_cost=1, white_cost=2, black_cost=1),
    Card(id=7, color=GREEN, total_cost=5, points=0,
        red_cost=1, green_cost=0, blue_cost=1, white_cost=1, black_cost=2),
    Card(id=8, color=BLUE, total_cost=5, points=0,
        red_cost=2, green_cost=1, blue_cost=0, white_cost=1, black_cost=1),
    Card(id=9, color=WHITE, total_cost=5, points=0,
        red_cost=1, green_cost=2, blue_cost=1, white_cost=0, black_cost=1),
    Card(id=10, color=BLACK, total_cost=5, points=0,
        red_cost=1, green_cost=1, blue_cost=2, white_cost=1, black_cost=0),

    #TODO card types 3-6

    # card type 7
    Card(id=31, color=RED, total_cost=3, points=0,
        red_cost=0, green_cost=0, blue_cost=0, white_cost=3, black_cost=0),
    Card(id=32, color=GREEN, total_cost=3, points=0,
        red_cost=3, green_cost=0, blue_cost=0, white_cost=0, black_cost=0),
    Card(id=33, color=BLUE, total_cost=3, points=0,
        red_cost=0, green_cost=0, blue_cost=0, white_cost=0, black_cost=3),
    Card(id=34, color=WHITE, total_cost=3, points=0,
        red_cost=0, green_cost=0, blue_cost=3, white_cost=0, black_cost=0),
    Card(id=35, color=BLACK, total_cost=3, points=0,
        red_cost=0, green_cost=3, blue_cost=0, white_cost=0, black_cost=0),

    #TODO card type 8

    # Level 2

    # card type 9
    Card(id=101, color=RED, total_cost=7, points=1,
        red_cost=2, green_cost=0, blue_cost=0, white_cost=2, black_cost=3),
    # green has type 1 and 2 reversed in table
    Card(id=102, color=GREEN, total_cost=7, points=1,
        red_cost=0, green_cost=0, blue_cost=3, white_cost=2, black_cost=2),
    Card(id=103, color=BLUE, total_cost=7, points=1,
        red_cost=3, green_cost=2, blue_cost=2, white_cost=0, black_cost=0),
    Card(id=104, color=WHITE, total_cost=7, points=1,
        red_cost=2, green_cost=3, blue_cost=0, white_cost=0, black_cost=2),
    Card(id=105, color=BLACK, total_cost=7, points=1,
        red_cost=0, green_cost=2, blue_cost=2, white_cost=3, black_cost=0),

    #TODO card types 9-14
    #Card(color=RED, total_cost=8, points=1),
    #Card(color=RED, total_cost=7, points=2),
    #Card(color=RED, total_cost=8, points=2),
    #Card(color=RED, total_cost=5, points=2),
    #Card(color=RED, total_cost=6, points=3),

    # Level 3

    #TODO card type 15
    #Card(color=RED, total_cost=14, points=3),

    # card type 16
    Card(id=206, color=RED, total_cost=7, points=4,
        red_cost=0, green_cost=7, blue_cost=0, white_cost=0, black_cost=0),
    Card(id=207, color=GREEN, total_cost=7, points=4,
        red_cost=0, green_cost=0, blue_cost=7, white_cost=0, black_cost=0),
    Card(id=208, color=BLUE, total_cost=7, points=4,
        red_cost=0, green_cost=0, blue_cost=0, white_cost=7, black_cost=0),
    Card(id=209, color=WHITE, total_cost=7, points=4,
        red_cost=0, green_cost=0, blue_cost=0, white_cost=0, black_cost=7),
    Card(id=210, color=BLACK, total_cost=7, points=4,
        red_cost=7, green_cost=0, blue_cost=0, white_cost=0, black_cost=0),

    # card type 17
    Card(id=211, color=RED, total_cost=12, points=0,
        red_cost=3, green_cost=6, blue_cost=3, white_cost=0, black_cost=0),
    Card(id=212, color=GREEN, total_cost=12, points=0,
        red_cost=0, green_cost=3, blue_cost=6, white_cost=3, black_cost=0),
    Card(id=213, color=BLUE, total_cost=12, points=0,
        red_cost=0, green_cost=0, blue_cost=3, white_cost=6, black_cost=3),
    Card(id=214, color=WHITE, total_cost=12, points=0,
        red_cost=3, green_cost=0, blue_cost=0, white_cost=3, black_cost=6),
    Card(id=215, color=BLACK, total_cost=12, points=0,
        red_cost=6, green_cost=3, blue_cost=0, white_cost=0, black_cost=3),

    #TODO card types 18-19
    #Card(color=RED, total_cost=12, points=4),
    #Card(color=RED, total_cost=10, points=5)
]
