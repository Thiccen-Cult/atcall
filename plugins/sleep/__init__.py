import time
ARGUMENTS = 1
def main(arg, cells, position):
    time.sleep(float(arg[0]))
    return {"cells": cells, "position": position}
