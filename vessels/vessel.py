from abc import ABCMeta, abstractmethod

class Vessel(metaclass = ABCMeta):

	def __init__(self, weapon,powerplant):
		self.weapon = weapon
		self.powerplant = powerplant
		print("Vessel object created...")

	@abstractmethod
	def powerup_plant(self):
		pass

	@abstractmethod 
	def shutdown_plant(self):
		pass

	@abstractmethod
	def aim_weapon(self):
		pass

	@abstractmethod
	def fire_weapon(self):
		pass 
