class Employee:

	def work(self):
		print("Employee Working")


class Manager(Employee):

	def manage(self):
		print("Managing Team")

class Devoloper(Employee):

	def code(self):
		print("Writing Python Code")

m1 = Manager()
m1.work()
m1.manage()

print("------------")

d1 = Devoloper()
d1.work()
d1.code()