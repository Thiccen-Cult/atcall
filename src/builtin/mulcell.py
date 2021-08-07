ARGUMENTS = 1
def main(arg: list, cells: dict, pos: int) -> dict:
    try:
        cells[pos] *= cells[int(arg[0])]
        return {"cells": cells, "pos": pos}
    except Exception as e:
        pass