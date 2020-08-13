class MachineExceptions(Exception):
	__module__ = Exception.__module__
	pass


class Error(MachineExceptions):
	def __init__(self):
		self.noSuchFileOrDirectory = "No such file or directory {file}."
		self.syntaxErrorMove = "Syntax error: can not move by to a non existent cell."
		self.notInt = "Syntax error: given value was not an integer."
		self.unkownError = "Syntax Error: unkown"
		self.noMainError = "No main function was provided."
	def noSuchFileOrDirectoryErr(self):
		raise MachineExceptions(self.noSuchFileOrDirectory)
	def syntaxErrorMoveErr(self):
		raise MachineExceptions(self.syntaxErrorMove)
	def notIntErr(self):
		raise MachineExceptions(self.notInt)
	def unkownErrorErr(self):
		raise MachineExceptions(self.unkownError)
	def noMainErrorErr(self):
		raise MachineExceptions(self.noMainError)

