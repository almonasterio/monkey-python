from objects.game import Game
from objects.pirate import Pirate
from objects.player import Player
from database import *

game = Game()

pirate = Pirate([i1, i3, i5])
pirate = Pirate([i2, i4, i6])
pirate = Pirate([i9, i8, i7])
pirate = Pirate([i10, i2, i4])
swordmaster = Pirate([im1,
                      im2,
                      im3,
                      im4,
                      im5,
                      im6,
                      im7,
                      im8,
                      im9,
                      im10,
                      im11])
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
                 im11], "alvaro")
while True:
    choice = game.show_menu()
    if choice == 1:
        game.combat(pirate, player)
    elif choice == 2:
        game.combat_swordmaster(swordmaster, player)
    elif choice == 3:
        exit()
