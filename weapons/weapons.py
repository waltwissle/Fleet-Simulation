from abc import ABCMeta, abstractmethod

class Weapon(metaclass = ABCMeta):

	def __init__(self):
		print("Weapon Object Created")

	@abstractmethod
	def aim(self):
		pass

	@abstractmethod
	def fire(self):
		pass
