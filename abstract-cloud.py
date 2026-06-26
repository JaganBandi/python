from abc import ABC , abstractmethod

class Cloud:

	@abstractmethod

	def deploy(self):
		pass

class AWS(Cloud)