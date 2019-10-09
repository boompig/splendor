from .colors import RED, GREEN, BLUE, WHITE, BLACK

class Noble:
    def __init__(self, points: int, total_amt: int,
                 red_amt: int, green_amt: int,
                 blue_amt: int, white_amt: int,
                 black_amt: int):
        """total_amt is used for error-checking"""
        self.points = points

        self.index = -1

        self.color_amounts = {
            RED: red_amt,
            GREEN: green_amt,
            BLUE: blue_amt,
            WHITE: white_amt,
            BLACK: black_amt
        }
        assert(self.color_amounts[RED] + self.color_amounts[GREEN] +\
                self.color_amounts[BLUE] + self.color_amounts[WHITE] +\
                self.color_amounts[BLACK] == total_amt)

    def __str__(self):
        return "Noble(RED={}, GREEN={}, BLUE={}, WHITE={}, BLACK={}".format(
                self.color_amounts[RED],
                self.color_amounts[GREEN],
                self.color_amounts[BLUE],
                self.color_amounts[WHITE],
                self.color_amounts[BLACK])

    def noble_applies(self, color_distribution):
        for color, amt in self.color_amounts.items():
            if color_distribution[color] < amt:
                return False
        return True

noble_list = [
    # nobles of type 1
    Noble(points=3, total_amt=8,
        red_amt=4, green_amt=4, blue_amt=0, white_amt=0, black_amt=0),
    Noble(points=3, total_amt=8,
        red_amt=0, green_amt=0, blue_amt=4, white_amt=4, black_amt=0),
    Noble(points=3, total_amt=8,
        red_amt=0, green_amt=0, blue_amt=0, white_amt=4, black_amt=4),
    Noble(points=3, total_amt=8,
        red_amt=0, green_amt=4, blue_amt=4, white_amt=0, black_amt=0),
    Noble(points=3, total_amt=8,
        red_amt=4, green_amt=0, blue_amt=0, white_amt=0, black_amt=4),

    # nobles of type 2
    Noble(points=3, total_amt=9,
        red_amt=3, green_amt=0, blue_amt=0, white_amt=3, black_amt=3),
    Noble(points=3, total_amt=9,
        red_amt=3, green_amt=3, blue_amt=3, white_amt=0, black_amt=0),
    Noble(points=3, total_amt=9,
        red_amt=0, green_amt=3, blue_amt=3, white_amt=3, black_amt=0),
    Noble(points=3, total_amt=9,
        red_amt=0, green_amt=0, blue_amt=3, white_amt=3, black_amt=3),
    Noble(points=3, total_amt=9,
        red_amt=3, green_amt=3, blue_amt=0, white_amt=0, black_amt=3),
]
for idx, noble in enumerate(noble_list):
    noble.index = idx
