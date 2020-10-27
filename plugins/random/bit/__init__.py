import random
def main(cells, position):
    cells[position] = random.choice([0, 1])
    return {"cells": cells, "position": position}