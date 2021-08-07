ARGUMENTS = 1
def main(arg: list, cells: dict, pos: int) -> dict:
    try:
        print(arg[0])
        return {"cells": cells, "pos": pos}
    except:
        pass