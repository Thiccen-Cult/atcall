> Plugins
Plugins allow you to add new builtin "functions" and you can have as many arguments passed to them as you want. <br>
<br>
A basic plugin has been placed in the `examples` directory. We will look at this. <br>

```py

ARGUMENTS = 2
def main(arg, cells, position):
    cells[position] = int(arg[0]) + int(arg[1])
    return {"cells": cells, "position": position}

```

<br>

First of all you are probably wondering how you decide upon the name of your builtin "function". You create a folder in the `plugins` directory with the name of the function. If I were to call `example` with the according arguments then it would work. The main function is the one which is called and has arguments passed to it when detected, this must be in the `__init__.py` file. <br>

If you want arguments you must define how many as `ARGUMENTS = {amount}` outside of any functions or classes and an `arg` argument in your main function. If you do not want arguments to be passed do not do that.

<br>

Arguments are passed via a list and every element is a string. The `cells` arguments is a dictionary containing the value of every cell and the `position` argument is an integer which is the current cell. If I want to alter the current cells value I would do `cells[position] = integer` because `cells` contains every cell in the structure of `{cell:value}` and `position` holds the current cells number.

<br>

You need to return a dictionary containing the cells and position like presented. This is to update any changes within atcall and is needed even if no data has been altered. They must be returned exactly as stated in that line. <br>

Everything else is up to you, have fun!

