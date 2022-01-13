class Python:	
	def __init__(self, name, age):		
		self.PythonName = name
		self.PythonAge = age
	def displayAge(self):
		print("Age: ", self.PythonAge)
obj = Python("R2J", 20)
print("Name: ", obj.PythonName)
obj.displayAge()
