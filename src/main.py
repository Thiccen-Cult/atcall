import sys, os, include.unix, include.windows
cells = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, -1: 0}
pos = 0
functions = {}

class Atcall:
    
    def __init__(self, program: str) -> None:
        global cells, pos, functions
        self.program = program
        self.cells = cells
        self.pos = pos
        self.functions = functions
        self.os = "unix"
    
    def parse(self, program: str) -> None:
        functions = program.lower().split("function")
        for i in functions:
            if len(i) > 0:
                self.functions[i.split()[0]] = i.split()[1:]
    
    def run(self, function: str = "main") -> None:
        self.parse(self.program)
        #print(self.functions)
        loop = -1
        #xyz = False
        for i in os.listdir("stdlib"):
            self.parse(open(os.path.join("stdlib", i), "r").read())
       
 #       for i in self.functions[function]:
  #          try:
    
        for i in self.functions[function]:
            loop += 1

            if (i not in ["incl", "if", "while", "call", "in", "rdint"]):
                try:
                    instruction = __import__(f"builtin.{i}", fromlist=[f"{i}"])
                    args = instruction.ARGUMENTS
                    data = instruction.main(self.functions[function][loop+1:loop+1+args], self.cells, self.pos)
                    self.cells = data["cells"]
                    self.pos = data["pos"]
                    #print(self.functions)
                    # for debugging: print(self.cells if xyz == True else "")
                except Exception as e:
                    pass

            elif (i in ["incl", "if", "while", "call", "in", "rdint"]):
                
                if i == "call":
                    try:
                        #xyz = True
                        self.run(self.functions[function][loop+1])
                    except:
                        pass
                elif i == "incl":
                    self.parse(open(self.functions[function][loop+1]+".atcl", "r").read())
                
                elif i == "in":
                    if self.os == "unix":
                        self.cells[pos] = ord(include.unix._input())
                    elif self.os == "windows":
                        self.cells[pos] = ord(include.unix_input())
                
                elif i == "rdint":
                    try:
                        if self.os == "unix":
                            self.cells[pos] = int(include.unix._input())
                        elif self.os == "windows":
                            self.cells[pos] = int(include.windows._input())
                    except:
                        self.cells[pos] = 0

                elif i == "if":
                    x = self.functions[function][loop+1]
                    y = self.functions[function][loop+3]
                    op = self.functions[function][loop+2]
                    iff = self.functions[function][loop+4]
                    elsef = self.functions[function][loop+5]
                    if op == "is":
                        if self.cells[int(x)] == int(y):
                            self.run(iff)
                        else:
                            self.run(elsef)
                    elif op == ">":
                        if self.cells[int(x)] > int(y):
                            self.run(iff)
                        else:
                            self.run(elsef)
                    elif op == "<":
                        if self.cells[int(x)] < int(y):
                            self.run(iff)
                        else:
                            self.run(elsef)
                    elif op == ">=":
                        if self.cells[int(x)] >= int(y):
                            self.run(iff)
                        else:
                            self.run(elsef)
                    elif op == "<=":
                        if self.cells[int(x)] <= int(y):
                            self.run(iff)
                        else:
                            self.run(elsef)
                    elif op == "!=":
                        if self.cells[int(x)] != int(y):
                            self.run(iff)
                        else:
                            self.run(elsef)

                elif i == "while":
                    x = self.functions[function][loop+1]
                    y = self.functions[function][loop+3]
                    op = self.functions[function][loop+2]
                    iff = self.functions[function][loop+4]
                    if op == "is":
                        while self.cells[int(x)] == int(y):
                            self.run(iff)
                    elif op == ">":
                        while self.cells[int(x)] > int(y):
                            self.run(iff)
                    elif op == "<":
                        while self.cells[int(x)] < int(y):
                            self.run(iff)
                    elif op == ">=":
                        while self.cells[int(x)] >= int(y):
                            self.run(iff)
                    elif op == "<=":
                        while self.cells[int(x)] <= int(y):
                            self.run(iff)
                    elif op == "!=":
                        while self.cells[int(x)] != int(y):
                            self.run(iff)
                            
Atcall(open(sys.argv[1], "r").read()).run()
