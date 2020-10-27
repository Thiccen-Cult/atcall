import random
ARGUMENTS = 2
def main(arg, cells, position):
    cells[position] = random.randrange(int(arg[0]), int(arg[1]))
    return {"cells": cells, "position": position}
