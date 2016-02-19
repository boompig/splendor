RED = 1
GREEN = 2
BLUE = 3
WHITE = 4
BLACK = 5


def color_to_string(color):
    if color == RED:
        return "RED"
    elif color == BLUE:
        return "BLUE"
    elif color == GREEN:
        return "GREEN"
    elif color == WHITE:
        return "WHITE"
    elif color == BLACK:
        return "BLACK"
    else:
        assert(False)
