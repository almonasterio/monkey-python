import random


class Pirate:
    def __init__(self, insults):
        self.insults_repo = insults
        self.life = 3
        # self.description="stinky pirate"
        # self.insults_used for future implementation
        self.lame_insults = ["I am afraid..",
                             "Oh ye-yeah..?", "Your mom fights like a cow"]

    def insult_action(self):
        insult_chosen = random.choice(self.insults_repo)
        insult_line = list(insult_chosen.keys())[0]
        print("Pirate says: ", insult_line)
        # print(self.insults_repo[insult_chosen.keys()])
        # Do I need to send the entire insult object?
        return insult_chosen

    def responds_back(self, insult_given):
        for i in self.insults_repo:
            if insult_given in list(i.keys()):
                print(f"Pirate says: {list(i.values())[0]}")
                return True
        print(random.choice(self.lame_insults))
        self.life -= 1
        return False
