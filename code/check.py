import datetime
from random import *
class Person:
	def __init__(self, name, age, ticket=None):
		self.name = name
		self.age = age
		self.ticket = ticket
		self.color = choice(["red",'blue','violet','pink','green'])

	def not_used_function(self):
		print(" I am not used")

	def check_access(self):
		if self.age > 18 and self.age < 50:
			return "Full Access"
		elif self.age < 18 and self.ticket == "e$23231":
			return "Limited Access"
		else:
			return "No Access"

	def get_birth_year(self):
		return datetime.date.today().year - self.age

if __name__ == '__main__':
	p1 = Person("Vegito", 23)
	print(p1.get_birth_year())
	print(p1.check_access())
