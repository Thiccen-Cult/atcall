ARGUMENTS = 0
def main(arg: list, cells: dict, pos: int) -> dict:
    try:
        cells[pos] = 0
        return {"cells": cells, "pos": pos}
    except Exception as e:
        pass