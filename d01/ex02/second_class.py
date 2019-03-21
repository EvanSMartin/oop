from first_class import MyClass
class SecondClass(MyClass):
	def __init__(self,name='ispirido'):
		self.say_hello(name)
		super().__init__()
