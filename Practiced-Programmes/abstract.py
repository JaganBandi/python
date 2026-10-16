from abc import ABC ,abstractmethod

class Employee(ABC):

	@abstractmethod
	def work(self):
		pass


class Devoloper(Employee):

	def work(self):
		print("Writing Python Code")

d1 = Devoloper()
d1.work()