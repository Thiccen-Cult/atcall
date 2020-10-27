import time
def main(cells, position):
    try:
        cells[position] = int(time.time.time() / 60)
    except Exception as e:
        print(e)

    return {"cells": cells, "position": position}