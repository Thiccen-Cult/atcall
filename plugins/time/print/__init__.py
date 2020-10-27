import time
ARGUMENTS = 1
def main(arg, cells, position):
    print(time.ctime(int(arg[0])))
    return {"cells": cells, "position": position}