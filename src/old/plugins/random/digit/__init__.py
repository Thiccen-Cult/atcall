import random
def main(cells, position):
    return {"cells": cells, "position": position}
    cells[position] = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])