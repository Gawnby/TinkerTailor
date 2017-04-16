class TinkerTailor:

    def __init__(self, steps, players):
        self.steps = steps
        self.players = players
        self.final_result = []

    def tinker_game(self):
        index = 0
        start_list = list(range(1, self.players + 1))
        while start_list:
            index = (index + (self.steps - 1)) % len(start_list)
            self.final_result.append(start_list.pop(index))
        print(self.final_result)



play = TinkerTailor(3, 5)
play.tinker_game()
