from first_class import MyClass
from random import *
class SecondClass(MyClass):
	def __init__(self, name='ispirido', hobby='lazy'):	
		self.hobby = hobby
		message = 'Hello, ' + str(name), 'your number is '  + self.roll_dice()
		self.hello(message)
		#super().__init__()

	def roll_dice(self):
		print('Method roll_dice is called from SecondClass')
		return str(randint(1,6))

	def get_hobby(self):
		return str(self.hobby)
