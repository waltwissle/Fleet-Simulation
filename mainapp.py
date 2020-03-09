
from weapons.turpedo import Turpedo
from weapons.ciws import Ciws
from powerplants.markvreactor import MarkVReactor
from powerplants.gasturbine import GasTurbine
from vessels.submarine import Submarine
from vessels.cruiser import Cruiser


def main():
	

	submarine = Submarine(Turpedo(), MarkVReactor())
	submarine.powerup_plant()
	submarine.aim_weapon()
	submarine.fire_weapon()
	submarine.shutdown_plant()

	print('-' * 30)

	cruiser = Cruiser(Ciws(),GasTurbine())
	cruiser.powerup_plant()
	cruiser.aim_weapon()
	cruiser.fire_weapon()
	cruiser.shutdown_plant()






if __name__ == "__main__":
	main()


