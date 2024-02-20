class A:
	def method1(self):
		print('This is method 1 of class A')
		
	def method2(self):
		print('feature_2 of class A')
	

class B(A):
	def method1(self):
		print('Modified method 1 of class A in class B') 
		
	def method3(self):
		print('feature_3 of class B')
		

obj = B()
obj.method1()
