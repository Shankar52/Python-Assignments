
class GFG1:
	def __init__(self):
		print('HEY !!!!!! GfG I am initialised(Class GEG1)')
	
	def sub_GFG(self, b):
		print('Printing from class GFG1:', b)
	def sub_gfg(self, b):
		print('Printing from class gfg1:', b)
	

class GFG2(GFG1):
	def __init__(self):
		print('HEY !!!!!! GfG I am initialised(Class GEG2)')
	
	def sub_GFG(self, b):
		print('Printing from class GFG2:', b)
		super().sub_GFG(b + 1)
	def sub_gfg(self, b):
		print('Printing from class gfg2:', b)
	

class GFG3(GFG2):
	def __init__(self):
		print('HEY !!!!!! GfG I am initialised(Class GEG3)')
	
	def sub_GFG(self, b):
		print('Printing from class GFG3:', b)
		super().sub_GFG(b + 1)
	def sub_gfg(self, b):
		print('Printing from class gfg3:', b)
	
	

if __name__ == '__main__':
	
	
	gfg = GFG3()
	gfg.sub_GFG(10)
	gfg.sub_gfg(10)
	gfg = GFG2()
	gfg.sub_GFG(10)
	gfg.sub_gfg(10)
	gfg = GFG1()
	gfg.sub_GFG(10)
	gfg.sub_gfg(10)


    
