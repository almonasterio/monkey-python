import random
from objects.game import Game
from objects.pirate import Pirate
from objects.player import Player
from database import *

game = Game()

pirate1 = Pirate(insults_repo1)
pirate2 = Pirate(insults_repo2)
pirate3 = Pirate(insults_repo3)
pirate4 = Pirate(insults_repo4)
pirate5 = Pirate(insults_repo5)
swordmaster = Pirate(insults_master_repo, "SwordMaster")
player = Player([im1,
                 im2,
                 im3,
                 im4,
                 im5,
                 im6,
                 im7,
                 im8,
                 im9,
                 im10,
                 im11], "Alvaro")
while True:
    choice = game.show_menu()
    if int(choice) == 1:
        game.combat(random.choice(
            [pirate1, pirate2, pirate3, pirate4, pirate5]), player)
    elif int(choice) == 2:
        game.combat_swordmaster(swordmaster, player)
    else:
        exit()
