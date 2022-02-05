class Game:
    def __init__(self):
        self.quit = False
        self.round = 0

    # def start(self):

# Create SwordMaster?

    def show_menu(self):
        return input("1.Play    2.Fight SwordMaster     3.Quit")

    def combat(self, first_pirate, second_pirate):
        while first_pirate.life and second_pirate.life:
            result = second_pirate.responds_back(first_pirate.insult_action())
            if result:
                first_pirate, second_pirate = second_pirate, first_pirate

        print(f"{first_pirate.name} annihilated {second_pirate.name}.")
        if first_pirate.player and first_pirate.life == 3:
            print(
                f"{second_pirate.name}: Wow.. you are good. You might be able to beat the Sword Master")
        first_pirate.life = 3
        second_pirate.life = 3

    def combat_swordmaster(self, swordmaster, player):
        while swordmaster.life and player.life:
            result = player.responds_back(swordmaster.insult_action())
            if result:
                swordmaster.life -= 1
        if swordmaster.life:
            winner, loser = swordmaster, player
            print(f"Keep trying.")
        else:
            winner, loser = player, swordmaster
            print(f"You won.")
            exit()
        print(f"{winner.name} annihilated {loser.name}.")
