import random
ARGUMENTS = 1
def main(arg, cells, position):
    cells[position] = random.randrange(0, int(arg[0]))
    return {"cells": cells, "position": position}