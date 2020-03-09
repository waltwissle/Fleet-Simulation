from vessels.vessel import Vessel

class Cruiser(Vessel):

	def __init__(self,weapon,powerplant):
		super(Cruiser, self).__init__(weapon, powerplant)
		print("Cruiser object created")

	def powerup_plant(self):
		self.powerplant.powerup()

	
	def shutdown_plant(self):
		self.powerplant.shutdown()

	
	def aim_weapon(self):
		self.weapon.aim()

	
	def fire_weapon(self):
		self.weapon.fire()

