from powerplants.powerplant import PowerPlant

class GasTurbine(PowerPlant):
	def __init__(self):
		super(GasTurbine, self).__init__() # This runs any initialization actions of the parent base class
		print('Gas Turbine object created')

	def powerup(self):
		print("GasTurbine is powered up and ready to answer all bells")

	def shutdown(self):
		print("GasTurbine is down.... cold and dark")