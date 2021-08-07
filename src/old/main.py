import errors, sys, os
cell = 0
funcs = {}
values = {}
class Main():
	def __init__(self):
		global cell, values, funcs
		self.move = "move"
		self.increase = "inc"
		self.decrease = "dec"
		self.copy = "cp"
		self.reset = "rst"
		self.set = "set"
		self.multiply = "mul"
		self.divide = "div"
		self.print = "print"
		self.func = "function"
		self.while_ = "while"
		self.is_ = "is"
		self.if_ = "if"
		self.then = "then"
		self.else_ = "else"
		self.new = "--new--"
		self.call = "call"
		self.input = "in"
		self.debug = "val"
		self.readInt = "rdint"
		self.nl =","
		self.add = "add"
		self.cell = cell
		self.values = values
		self.funcs = funcs
		self.os = "unix" # change to "windows" for windows	
		self.import_ = "incl"
	def function(self,text):
		try:
			text = text.lower()
			cont = text.split(self.func)
			cont2 = text.split()
			for i in cont:
				t = i
				i = i.split()
				if len(i) > 0:
					self.funcs[i[0]] = i[1:]
			loop = -1
			for i in cont2:
				loop += 1
				#print(i)
				if i == self.import_:
					try:
						#print(os.getcwd())
						self.function(open((os.path.join(os.getcwd(),cont2[loop+1].lower()+".atcl")),"r").read())
					except Exception as e:
						print(e)
						print("Failed to import ''. Does it exist?")

			#print(self.funcs)
		except:
			pass
			#print(e)
		#print(self.funcs)

	def parse(self,x="main"):
		try:
			loop = -1

			for i in self.funcs:
				if i == x:
					#self.funcs[i] = ' '.join(self.funcs[i]).split(";")[0].split()
					#print(self.funcs[i])
					for t in self.funcs[i]:
						loop += 1
						#print(t) 
						try:
							if self.funcs[i][loop+1] == "?":
								self.funcs[i][loop+1] = self.cell
							elif self.funcs[i][loop+1] == "!":
								self.funcs[i][loop+1] = self.values[self.cell]
						except:
							pass
						if t == self.move:
							try:
								self.cell = int(self.funcs[i][loop+1])
							except:
								print(f"{t.upper()} {self.funcs[i][loop+1]}")
								errors.Error().notIntErr()
						elif t == self.increase:
							try:
								self.values[self.cell] += int(self.funcs[i][loop+1])
							except KeyError:
								self.values[self.cell] = int(self.funcs[i][loop+1])
							except ValueError:
								print(f"{t.upper()} {self.funcs[i][loop+1]}")
								errors.Error().notIntErr()
						elif t == self.decrease:
							try:
								if self.values[self.cell] > 0:
									self.values[self.cell] -= int(self.funcs[i][loop+1])
								else:
									self.values[self.cell] = 0
							except KeyError:
								self.values[self.cell] = 0
							except ValueError:
								print(f"{t.upper()} {self.funcs[i][loop+1]}")
								errors.Error().notIntErr()
						elif t == self.copy:
							try:
								self.values[int(self.funcs[i][loop+2])] = self.values[int(self.funcs[i][loop+1])]
							except Exception as e:
								print(e)
								self.values[int(self.funcs[i][loop+2])] = 0
						elif t == self.set:
							try:
								self.values[self.cell] = int(self.funcs[i][loop+1])
							except KeyError:
								self.values[self.cell] = int(self.funcs[i][loop+1])
							except ValueError:
								print(f"{t.upper()} {self.funcs[i][loop+1]}")
								errors.Error().notIntErr()
						elif t == self.multiply:
							try:
								self.values[self.cell] *= int(self.funcs[i][loop+1])
							except KeyError:
								self.values[self.cell] = 0
							except ValueError:
								print(f"{t.upper()} {self.funcs[i][loop+1]}")
								errors.Error().notIntErr()
						elif t == self.divide:
							try:
								if self.values[self.cell] > 0:
									self.values[self.cell] /=  int(self.funcs[i][loop+1])
									self.values[self.cell] = int(self.values[self.cell])
								else:
									self.values[self.cell] = 0
							except KeyError:
								self.values[self.cell] = 0
							except ValueError:
								print(f"{t.upper()} {self.funcs[i][loop+1]}")
								errors.Error().notIntErr()
						elif t == self.print:
							try:
								#pass
								print(chr(self.values[self.cell]),end="")
							except Exception as e:
								#print(e)
								pass
						elif t == self.debug:
							try:
								#pass
								print(self.values[self.cell],end="")
							except Exception as e:
								#print(e)
								pass
						elif t == self.input:
							try:
								if self.os == "unix":
									import unix
									self.values[self.cell] = ord(unix._input())
								elif self.os == "windows":
									import windows
									self.values[self.cell] = ord(windows._input())

							except Exception as e:
								#print(e)
								self.values[self.cell] = 0
						elif t == self.while_:
							try:
								x = self.funcs[i][loop+2]
								if x == self.is_:
									while self.values[int(self.funcs[i][loop+1])] == int(self.funcs[i][loop+3]):
										Main().parse(x=self.funcs[i][loop+4])
								elif x == ">":
									while self.values[int(self.funcs[i][loop+1])] > int(self.funcs[i][loop+3]):
										Main().parse(x=self.funcs[i][loop+4])
								elif x == ">=":
									while self.values[int(self.funcs[i][loop+1])] >= int(self.funcs[i][loop+3]):
										Main().parse(x=self.funcs[i][loop+4])
								elif x == "<":
									while self.values[int(self.funcs[i][loop+1])] < int(self.funcs[i][loop+3]):
										Main().parse(x=self.funcs[i][loop+4])
								elif x == "<=":
									while self.values[int(self.funcs[i][loop+1])] <= int(self.funcs[i][loop+3]):
										Main().parse(x=self.funcs[i][loop+4])
								elif x == "!=":
									while self.values[int(self.funcs[i][loop+1])] != int(self.funcs[i][loop+3]):
										Main().parse(x=self.funcs[i][loop+4])
							except Exception as e:
								print(e)
								print("error")
						elif t == self.if_:
							try:
								x = self.funcs[i][loop+2]

								if x == self.is_:
									if self.values[int(self.funcs[i][loop+1])] == int(self.funcs[i][loop+3]):
										Main().parse(x=self.funcs[i][loop+4])
									else:
										Main().parse(x=self.funcs[i][loop+5])
								elif x == ">":
									if self.values[int(self.funcs[i][loop+1])] > int(self.funcs[i][loop+3]):
										Main().parse(x=self.funcs[i][loop+4])
									else:
										Main().parse(x=self.funcs[i][loop+5])
								elif x == ">=":
									if self.values[int(self.funcs[i][loop+1])] >= int(self.funcs[i][loop+3]):
										Main().parse(x=self.funcs[i][loop+4])
									else:
										Main().parse(x=self.funcs[i][loop+5])
								elif x == "<":
									if self.values[int(self.funcs[i][loop+1])] < int(self.funcs[i][loop+3]):
										Main().parse(x=self.funcs[i][loop+4])
									else:
										Main().parse(x=self.funcs[i][loop+5])
								elif x == "<=":
									if self.values[int(self.funcs[i][loop+1])] <= int(self.funcs[i][loop+3]):
										Main().parse(x=self.funcs[i][loop+4])
									else:
										Main().parse(x=self.funcs[i][loop+5])

								elif x == "!=":
									if self.values[int(self.funcs[i][loop+1])] != int(self.funcs[i][loop+3]):
										Main().parse(x=self.funcs[i][loop+4])
									else:
										Main().parse(x=self.funcs[i][loop+5])

							except Exception as e:
								#raise
								print("error")
						elif t == self.call:
							try:
								#print(self.funcs[self.funcs[i][loop+1]])
								y =self.funcs[i][loop+1]
								#print(x)
								Main().parse(x=y)					
							except Exception as e:
								raise
								pass
						elif t == self.readInt:
							try:
								if self.os == "unix":
									import unix
									self.values[self.cell] = int(unix._input().encode().decode())
								elif self.os == "windows":
									import windows
									self.values[self.cell] = int(windows._input().encode().decode())

							except Exception as e:
								#raise
								#print(e)
								self.values[self.cell] = 10
						elif t == "pass":
							pass
						elif t == self.reset:
							self.values[self.cell] = 0
						elif t == self.add:
							try:
								self.values[self.cell] += self.values[int(self.funcs[i][loop+1])]
							except KeyError:
								self.values[self.cell] = self.values[int(self.funcs[i][loop+1])]
							except ValueError:
								print(f"{t.upper()} {self.funcs[i][loop+1]}")
								errors.Error().notIntErr()
						elif t == "mulcell":
							try:
								self.values[self.cell] *= int(self.values[int(self.funcs[i][loop+1])])
							except KeyError:
								#print("p")
								self.values[self.cell] = 0
							except ValueError:
								print(f"{t.upper()} {self.funcs[i][loop+1]}")
								errors.Error().notIntErr()

						elif t == "divcell":
							try:
								self.values[self.cell] = int(self.values[self.cell] / int(self.values[int(self.funcs[i][loop+1])]))
							except KeyError:
								#print("p")
								self.values[self.cell] = 0
							except ValueError:
								print(f"{t.upper()} {self.funcs[i][loop+1]}")
								errors.Error().notIntErr()
							#except:
								#raise
						else:
							try:
								x = __import__(f"plugins.{t}", fromlist=[f'{t}'])
								try:
									#print()
									ret = x.main(self.funcs[i][loop+1:loop+1+x.ARGUMENTS], self.values, self.cell)
									self.values = ret["cells"]
									self.cell = ret["position"]
								except (TypeError, AttributeError) as e:
									#print(e)
									ret = x.main(self.values, self.cell)
									self.values = ret["cells"]
									self.cell = ret["position"]
							except Exception as e:
								pass
								#print(e)
					#print(self.cell,self.values)


						#print(self.values)
		except Exception as e:
			raise
			#print(e)
			print("No main function was providied.")


f = open(sys.argv[1],"r").read()
Main().function(f)
#print(Main().funcs)
Main().parse()
