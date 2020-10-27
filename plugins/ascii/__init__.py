ARGUMENTS = 1
def main(arg, cells, position):
    cells[position] = ord(arg[0])
    return {"cells": cells, "position": position}
