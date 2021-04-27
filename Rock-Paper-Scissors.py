import random


class Game:
    # computer_loses = {'roc k': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    computer_wins = {'scissors': 'rock', 'rock': 'paper', 'paper': 'scissors'}
    computer_wins_2 = {}
    default_game_range = ['scissors', 'paper', 'rock']

    def __init__(self):
        self.name = input('Enter your name:\n')
        self.value = 0
        print(f'\nHello, {self.name}!\n')
        self.new_game_range = []
        Game.ranking(self)  # immediately rewrites 0 after creating a new person
        Game.game_possibilities(self)
        Game.rules(self)

    def game_possibilities(self):
        self.attributes = str(input("Your game attributes - enter the fighting elements or or skip (enter) and play "
                                    "the default mode:\n"))
        if len(self.attributes) == 0:
            self.new_game_range = Game.default_game_range
            print(f"Standard choices in the game:{self.new_game_range}\nOkay, let's start!")
        else:
            if ',' in self.attributes:
                self.new_game_range = self.attributes.split(",")
            else:
                self.new_game_range = self.attributes.split(" ")
            print(f"\nNew possibilities choices in the game:{self.new_game_range}\nOkay, let's start!")

    def ranking(self):
        file = open('rating.txt', 'r+')
        text = file.read()
        lst = text.split()  # convert text to list
        ranking = Game.convert(lst)
        if self.name in lst:
            result = ranking[self.name]
            return result
        else:
            self.value = 0
            file.write(f'\n{self.name} {self.value}')
        file.close()

    def new_score(self):
        file = open('rating.txt', 'r+')
        text = file.read()
        lst = text.split()
        ranking = Game.convert(lst)
        file.close()
        if self.value > 0:
            new_score = int(ranking[self.name]) + self.value
            old_person_data = '{} {}'.format(self.name, ranking[self.name])
            new_person_data = '{} {}'.format(self.name, new_score)
            txt2 = text.replace(old_person_data, new_person_data, 1)
            file = open('rating.txt', 'w')
            file.write(txt2)
        file.close()

    def convert(lst):
        repl_dictionary = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
        # points were assigned as values to a given person (key)
        return repl_dictionary

    def clash_default(self):
        if self.computer_choice == self.player_choice:
            print(f'There is a draw ({self.computer_choice})')
            self.value = 50
            Game.new_score(self)
        elif self.player_choice == Game.computer_wins[self.computer_choice]:
            print(f'Well done. The computer chose {self.computer_choice} and failed')
            self.value = 100
            Game.new_score(self)
        else:  # (player_choice == computer_loses[player_choice]:
            print(f'Sorry, but the computer chose {self.computer_choice}')
            self.value = 0
            Game.new_score(self)

    def clash_new(self):
        check = (Game.computer_wins_2[self.computer_choice])
        if self.computer_choice == self.player_choice:
            print(f'There is a draw ({self.computer_choice})')
            self.value = 50
            Game.new_score(self)
        elif self.player_choice in check:
            print(f'Well done. The computer chose {self.computer_choice} and failed')
            print(f'{self.computer_choice} only loses with {check}')
            self.value = 100
            Game.new_score(self)
        else:  # (player_choice == computer_loses[player_choice]:
            print(f'Sorry, but the computer chose {self.computer_choice}')
            print(f'{self.computer_choice} only loses with {check}')
            self.value = 0
            Game.new_score(self)

    def rules(self):
        max_range = self.new_game_range + self.new_game_range
        half_range = (len(self.new_game_range) // 2) + 1
        for self.element in self.new_game_range:
            # {element: [winning elements]}
            # print({(self.new_game_range[self.new_game_range.index(self.element)]):
            # (max_range[self.new_game_range.index(self.element) + 1:
            # self.new_game_range.index(self.element) + half_range])})
            self.element = {(self.new_game_range[self.new_game_range.index(self.element)]):
                                (max_range[self.new_game_range.index(self.element) + 1: self.new_game_range.index(
                                    self.element) + half_range])}
            Game.computer_wins_2.update(self.element)

    def choose(self, player_choice):
        self.player_choice = player_choice
        self.computer_choice = random.choice(self.new_game_range)
        if self.player_choice in self.new_game_range:
            if len(self.attributes) == 0:
                self.clash_default()
                return True
            else:
                self.clash_new()
                return True
        elif self.player_choice == 'Rating':
            print(Game.ranking(self))
            return True
        elif self.player_choice == 'Exit':
            print('Bye!')
            return False
        else:
            print('Invalid input')
            return True


game = Game()
while game.choose(input('\nChoose: an element to fight / Rating / Exit\n')):
    pass