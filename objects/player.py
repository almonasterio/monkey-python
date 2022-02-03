from .pirate import Pirate


class Player(Pirate):
    def __init__(self, name="Guybrush"):
        # super().__init__(insults={})
        super().__init__(insults=[{"insult5": "response5"},  {"insult": "response"},
                                  {"insult2": "response2"}])
        self.name = name
        self.insults_lines = list(map(lambda insult: list(
            insult.keys())[0], self.insults_repo))

    def display_my_repo_lines(self, list):
        for i in enumerate(list):
            print(f"* {i[1]}")

    def insult_action(self):
        while True:
            self.display_my_repo_lines(self.insults_lines)
            chosen_insult_line = input(
                f"{self.name} type your insult of choice: ")
            if chosen_insult_line not in self.insults_lines:
                print("Oh ok, good try... now try again")
                continue
            return chosen_insult_line

    def responds_back(self, insult_given):
        insult_given_line, insult_given_response = list(
            insult_given.items())[0]
        if insult_given_line not in self.insults_lines:
            self.insults_lines.append(insult_given_line)
        my_response_lines = list(map(lambda insult: list(
            insult.values())[0], self.insults_repo))+self.lame_insults
        self.display_my_repo_lines(my_response_lines)
        while True:
            chosen_response_line = input(
                f"{self.name}, pick your respond to such an insult ")
            if chosen_response_line not in my_response_lines:
                print("Oh ok, good try... now try again")
                continue
            # if list(insult_given.values())[0] == chosen_response_line:
            if insult_given_response == chosen_response_line:
                print("Good answer")
                return True
            print("Bad answer")
            self.life -= 1
            return False
