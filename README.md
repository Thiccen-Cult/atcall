# atcall

Please see https://en.wikipedia.org/wiki/Esoteric_programming_language on information on what an esoteric programming language (esolang) is if you did not already know. <br>

> Note: the only whitespace required is that between an instruction and its argument and atcall is not require uppercase to be used.

<br>

> Note: The ? and ! placeholders have only been implemented in the old version of atcall in old/

<br>

> Note: If you want to load plugins add them to the src/builtin folder. They will function the same as prior to the rewrite. 

<br>

An esoteric "programming language" written in 20 minutes with python 3. <br>

If you are using windows please change `self.os` in `main.py` to `"windows"`. <br>

Please see the folder `examples` for examples. <br>

By [Polarz](https://github.com/Polarzz/) <br>

Usage `<your systems python command> main.py <path/to/file/to/run.py>` <br>

Does not have proper error handling of any sort, wasn't meant to be good, was created in 20 minutes. <br>

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
PRINT (no arguments, prints a char based off the ascii value of the current cell)
VAL (no arguments, prints the value of the current cell)
IN (no arguments, sets the current cells value to the ascii code of a character of input from the user)
RDINT (no arguments, same as IN but only accepts ints as input and returns the actual integer instead of its ascii code)
IF (cell) (IS | > | < | >= | <= | != ) (value) (function name to execute if) (function name to execute else)
WHILE (cell) (IS | > | < | >= | <= | !=) (value) (function name to execute)
PASS (no arguments, does nothing)
CALL (functions name to execute)
INCL (file name without extension to include)
ADD (cell number) (cell number) (will set the first given cell number to the value of both, this is not an arg but an explanation)
MULCELL (cell number) (multiplies current cell by another)
DIVCELL (cell number) (divides current cell by another)
```

IF you want to pass the current cells value to one of these instructions you can use `!`.

```hs
FUNCTION MAIN
  SET 10
  MUL !
  VAL
```

Output: 100 <br>

There is also a `?` placeholder which contains the current position within the cells. <br>

`RDINT` will return `10` on invalid input as you can only input 0-9 so it made sense to make it return a value that could not be entered. <br>

<br>

atcall will automaticaly run the `MAIN` function. <br>

e.g

```hs
FUNCTION MAIN
  MOVE 0
  SET 10
  PRINT
 ```
 
 or for multiple functions<br>
 ```hs
 FUNCTION PRINT_NEW_LINE
  MOVE 0
  SET 10
  PRINT

FUNCTION MAIN
  CALL PRINT_NEW_LINE
 ```
 
 Both of these programs will print an empty (new) line. <br>
 
 Import example: <br>
 import.actl
 
 ```hs
 FUNCTION MAIN
  SET 10
  PRINT
  ```

main.actl<br>
  
```hs
FUNCTION MAIN
  INCL import
```
 
This will call the main function from `import.actl` as if it were it were `main.actl`'s main function. <br>
If you have functions in another and include that file, all functions would be imported as if they were defined in your main file. <br>
Example: <br>
import.actl <br>
 
 ```hs
 FUNCTION PRINT_NEW_LINE
  SET 10
  PRINT
```
  
main.actl <br>

```hs
  FUNCTION MAIN
    INCL import
    CALL PRINT_NEW_LINE
```

This will print a newline <br>
