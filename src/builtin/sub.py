ARGUMENTS = 2
def main(arg: list, cells: dict, pos: int) -> dict:
    try:
        cells[int(arg[0])] -= cells[int(arg[1])]
        return {"cells": cells, "pos": pos}
    except Exception as e:
        pass