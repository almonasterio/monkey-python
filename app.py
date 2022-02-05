from objects.game import Game
from objects.pirate import Pirate
from objects.player import Player
# from database import *

game = Game()
choice = game.show_menu()

# while choice != 2:
#     choice = game.show_menu()

insults_repo = [
    {"i1": "r1"},
    {"i2": "r2"},
    {"i3": "r3"}]

insults_repo2 = [
    {"i6": "r6"},
    {"i2": "r2"},
    {"i3": "r3"}]
pirate = Pirate(insults_repo)
player = Player(insults_repo2)
print(player.name)
print(pirate.name)
# pirate.responds_back(player.insult_action())
# winner = pirate
# loser = player

# game.combat(pirate, player)
game.combat_swordmaster(pirate, player)
