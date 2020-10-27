import random, time
def main(cells, position):
    cells[position] = random.randrange(0, int(time.time()))
    return {"cells": cells, "position": position}
