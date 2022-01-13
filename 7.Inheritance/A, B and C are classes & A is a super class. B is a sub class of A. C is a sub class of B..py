class A:
	def method1(self):
		print ('pythonlearning1.com')
	def method2(self):
		print ('pythonlearning2.com')
	def method3(self):
		print ('pythonlearning3.com')

		
class B(A):
	def method4(self):
		print ('www.pythonlearning4.com')
	def method5(self):
		print ('www.pythonlearning5.com')
	def method6(self):
		print ('www.pythonlearning6.com')
	
class C(B):
	def method7(self):
		print ('www.pythonlearn7.com')
	def method8(self):
		print ('www.pythonlearn8.com')
	def method9(self):
		print ('www.pythonlearn9.com')



		
a=C()
a.method1()
a.method2()
a.method3()
a.method4()
a.method5()
a.method6()
a.method7()
a.method8()
a.method9()
