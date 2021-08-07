import time
def main(cells, position):
    try:
        cells[position] = int(time.time.time())
    except Exception as e:
        print(e)

    return {"cells": cells, "position": position}