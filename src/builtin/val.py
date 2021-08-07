ARGUMENTS = 0
def main(arg: list, cells: dict, pos: int) -> dict:
    try:
        print(cells[pos], end="")
        return {"cells": cells, "pos": pos}
    except Exception as e:
        pass