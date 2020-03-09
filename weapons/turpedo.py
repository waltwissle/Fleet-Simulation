from weapons.weapons import Weapon

class Turpedo(Weapon):
	def __init__(self):
		super(Turpedo, self).__init__() # the super key-word is used to initialize (basically run the parent class) the class being inherited.
		print('Torpedo object created')

	def aim(self):
		print("Torpedo is aimed and ready to fire!")

	def fire(self):
		print("Torpedo away..... swoosh.. zzzzzzz KABOMM!! -Target Destroyed!!")
