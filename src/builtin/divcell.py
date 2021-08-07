ARGUMENTS = 2
def main(arg: list, cells: dict, pos: int) -> dict:
    try:
        cells[pos] /= cells[int(arg[0])]
        cells[pos] = int(cells[pos])
        return {"cells": cells, "pos": pos}
    except Exception as e:
        pass