import random


class NumberGuesser:
    START = 0
    END = 10

    def __init__(self):
        self.random_num = random.randint(self.START, self.END)
        print(f"Clue:  {self.random_num}")

    def __validate_number(self, number: int):
        print(number)
        if number < self.random_num:
            print("Number too low")
        elif number > self.random_num:
            print("Number too high")
        else:
            return True

    def start_game(self):
        print(f"Welcome to Number Guesser \n Guess the number between {self.START} and {self.END}")
        while True:
            number = int(input("Guess the number ==> "))
            if self.__validate_number(number):
                print("You won!!!")
                break


if __name__ == '__main__':
    NumberGuesser().start_game()
