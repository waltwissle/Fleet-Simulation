from weapons.weapons import Weapon

class Ciws(Weapon):
	'''
	Closed-In Weapon Systems
	'''
	def __init__(self):
		super(Ciws, self).__init__()
		print('CIWS object created')

	def aim(self):
		print("CIWS is aimed and ready to fire!")

	def fire(self):
		print("CIWS away..... swoosh.. zzzzzzz KABOMM!! - Target Destroyed!!")

