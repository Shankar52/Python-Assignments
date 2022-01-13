class Bmw:
        def __init__(self):
                self.models = ['i8', 'x1', 'x5', 'x6']
        
        def outModels(self):
                print('These are the available models for BMW')
                for model in self.models:
                        print('\t%s ' % model)

class Audi:
	def __init__(self):
		self.models = ['q7', 'a6', 'a8', 'a3']
		
	def outModels(self):
		print('These are the available models for Audi')
		for model in self.models:
			print('\t%s ' % model)



import BmwandAudi

if __name__ == '__main__':

    a=BmwandAudi.Bmw()
    a.outModels()

    b=BmwandAudi.Audi()
    b.outModels()


