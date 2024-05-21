class PlayerCharacter:
    def __init__(self):
        self.__create_name()

    def __create_name(self):
        while True:
            char = input("Insert char for player - >")
            if len(char) == 1:
                break
            print("Player name must be only one character")
        self.__character_name = char

    @property
    def name(self):
        return self.__character_name


class Match:
    DEFAULT_CELLS = [["O", "O", "O"],
                     ["O", "O", "O"],
                     ["O", "O", "O"]]

    def __init__(self, players: list[PlayerCharacter]):
        self.players = players
        self.game_cells = self.DEFAULT_CELLS

    def __iter__(self):
        return self

    def __next__(self):
        return "a"

    def __print_current_game(self):
        x = self.game_cells
        print(f"""
                {x[0][0]}\t|\t{x[0][1]}\t|\t{x[0][2]}
                ------------------    
                {x[1][0]}\t|\t{x[1][1]}\t|\t{x[1][2]}
                ------------------
                {x[2][0]}\t|\t{x[2][1]}\t|\t{x[2][2]}
                """)


class Game:
    TOTAL_PLAYERS = 2

    def __init__(self):
        self.players: list[PlayerCharacter] = []
        self.__create_players()
        self.turn = 0

    def __iter__(self):
        return self

    def __next__(self):
        match = self.__create_match()
        self.__start_match()
        for instance in match:
            print(f"Turn of player  {self.players[0]}")

    def __create_players(self):
        for i in range(self.TOTAL_PLAYERS):
            print(f"For Player {i}:")
            self.players.append(PlayerCharacter())

    def __create_match(self):
        return Match(players=self.players)

    def __start_match(self):
        pass

    def new_game(self):
        current_match: Match = self.__create_match()

    def infinite_games(self):
        for match in self:
            print("s")


if __name__ == '__main__':
    Game = Game()
    Game.infinite_games()
