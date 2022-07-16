import re


class Player:
    def __init__(self, name:str):
        self.name = name
        self.score = 0

    def update_score(self, new_score:int):
        self.score += new_score

    def make_guess(self, guess:str):
        occurnece= len(re.findall(f'(?={guess})', S))
        print(occurnece)
        self.update_score(occurnece)
        





if __name__ == "__main__":
    S='BANANA'
    Kevin= Player('Kaven')
    Stuart= Player('Stuart')
    round = 0

    while True:
        guess= str(input(f'{Kevin.name} please enter a guess: '))
        Kevin.make_guess(guess)
        guess= str(input(f'{Stuart.name} please enter a guess: '))
        Stuart.make_guess(guess)

        round+= 1
        if round==10:
            break


    if Kevin.score > Stuart.score:
        print(f'{Kevin.name} is the winner and his score is {Kevin.score}')
    elif Kevin.score < Stuart.score:
        print(f'{Stuart.name} is the winner and his score is {Stuart.score}')

    else:
        print('ITs a draw')

