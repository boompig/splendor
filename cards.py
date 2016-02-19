class Card(object):
    def __init__(self, cost, points, color):
        self.cost = cost
        self.points = points
        self.color = color

    def __str__(self):
        return "Card (color={}, cost={}, points={})".format(
                self.color, self.cost, self.points)

# colors
RED = 1
GREEN = 2
BLUE = 3
WHITE = 4
BLACK = 5

# there are different distributions for gems
card_list = [
    # Level 1
    Card(color=RED, cost=4, points=0),
    Card(color=GREEN, cost=4, points=0),
    Card(color=BLUE, cost=4, points=0),
    Card(color=WHITE, cost=4, points=0),
    Card(color=BLACK, cost=4, points=0),

    Card(color=RED, cost=5, points=0),
    Card(color=GREEN, cost=5, points=0),
    Card(color=BLUE, cost=5, points=0),
    Card(color=WHITE, cost=5, points=0),
    Card(color=BLACK, cost=5, points=0),

    Card(color=RED, cost=3, points=0),
    Card(color=RED, cost=4, points=1),
    # Level 2
    Card(color=RED, cost=7, points=1),
    Card(color=RED, cost=8, points=1),
    Card(color=RED, cost=7, points=2),
    Card(color=RED, cost=8, points=2),
    Card(color=RED, cost=5, points=2),
    Card(color=RED, cost=6, points=3),
    # Level 3
    Card(color=RED, cost=14, points=3),
    Card(color=RED, cost=7, points=4),
    Card(color=RED, cost=12, points=4),
    Card(color=RED, cost=10, points=5)
]
