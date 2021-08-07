ARGUMENTS = 2
def main(arg, cells, position):
    try:
        cells[int(arg[0])] -= cells[int(arg[1])]
    except Exception as e:
        pass
    return {"cells": cells, "position": position}