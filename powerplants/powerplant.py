from abc import ABCMeta, abstractmethod

class PowerPlant(metaclass = ABCMeta):

	def __init__(self):
		print("PowerPlant object created...")

	@abstractmethod
	def powerup(self):
		pass

	@abstractmethod
	def shutdown(self):
		pass 