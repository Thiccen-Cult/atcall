ARGUMENTS = 1
def main(arg: list, cells: dict, pos: int) -> dict:
    try:
        pos = int(arg[0])
        return {"cells": cells, "pos": pos}
    except Exception as e:
        pass