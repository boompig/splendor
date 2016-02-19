class Card(object):
    def __init__(self, cost, points):
        self.cost = cost
        self.points = points

    def __str__(self):
        return "Card (cost=%d, points=%d)" % (self.cost, self.points)
        
# there are different distributions for gems
card_list = [
    # Level 1
    Card(cost=4, points=0),
    Card(cost=5, points=0),
    Card(cost=3, points=0),
    Card(cost=4, points=1),
    # Level 2
    Card(cost=7, points=1),
    Card(cost=8, points=1),
    Card(cost=7, points=2),
    Card(cost=8, points=2),
    Card(cost=5, points=2),
    Card(cost=6, points=3),
    # Level 3
    Card(cost=14, points=3),
    Card(cost=7, points=4),
    Card(cost=12, points=4),
    Card(cost=10, points=5)
]
