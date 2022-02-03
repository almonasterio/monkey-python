from objects.game import Game
from objects.pirate import Pirate
from objects.player import Player
# from database import *

game = Game()
choice = game.show_menu()

# while choice != 2:
#     choice = game.show_menu()

insults_repo12 = [
    {"insult6": "response1"},
    {"insult62": "response2"},
    {"insult63": "response3"}]
pirate = Pirate(insults_repo12)
print(pirate.insults_repo)
player = Player()

# print(pirate.life)
# pirate.responds_back(player.insult_action())

player.insult_action()
player.responds_back(pirate.insult_action())
print(player.life)
player.responds_back(pirate.insult_action())
print(player.life)
player.insult_action()
