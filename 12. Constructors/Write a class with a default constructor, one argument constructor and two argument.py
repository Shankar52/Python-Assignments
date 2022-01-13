class example:

	def __init__(self):
		print("One")

	def __con__(self,x=10):
		print("Two")

	def __repr__(self,x=5,y="Two"):
		print("Three")


e = example()
e.__init__()
e.__con__()
e.__repr__()
