from powerplants.powerplant import PowerPlant

class MarkVReactor(PowerPlant):
	def __init__(self):
		super(MarkVReactor, self).__init__()
		print('MarkVReactor object created')

	def powerup(self):
		print("MarkVReactor is powered up and ready to answer all bells")

	def shutdown(self):
		print("MarkVReactor is down.... cold and dark")