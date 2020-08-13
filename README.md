# atcall
An esoteric "programming language" written in 20 minutes with python 3. <br>
If you are using windows please change `self.os` in `main.py` to `"windows"`. <br>
<h1> Information </h1>
atcall has quite a few instructions. <br>

```hs
MOVE (cell number to move to)
SET (value to set current cell to)
INC (value to increase current cell by)
DEC (value to decrease current cell by)
MUL (value to multiply current cell by)
DIV (value to divide current cell by)
RST (no arguments, resets current cell)
CP (cell to copy value of) (cell to set copied value to)
PRINT (no arguments, prints a char based of the ascii value of the current cell)
VAL (no arguments, prints the value of the current cell)
IN (no arguments, sets the current cells value to the ascii code of a character of input from the user)
RDINT (no arguments, same as IN but only accepts ints as input and returns the actual integer instead of its ascii code)
IF (cell) (IS | > | < | >= | <= | != ) (value) (function name to execute if) (function name to execute else)
WHILE (cell) (IS | > | < | >= | <= | !=) (value) (function name to execute)
PASS (no arguments, does nothing)
CALL (functions name to execute)
```
<br>

atcall will automaticaly run the `MAIN` function. You need to use `--NEW--` when defining a new function. <br>

e.g

```hs
--NEW--
FUNCTION MAIN
  MOVE 0
  SET 10
  PRINT
 ```
 
 or for multiple functions<br>
 ```hs
 --NEW--
 FUNCTION PRINT_NEW_LINE
  MOVE 0
  SET 10
  PRINT
  
--NEW--
FUNCTION MAIN
  CALL PRINT_NEW_LINE
 ```
 

