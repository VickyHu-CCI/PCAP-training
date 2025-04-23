
from models.player import HumanPlayer, ComputerPlayer
from models.game import Game


def main():
    print('--- Rock Paper Scissors Game ---')
    # while True:
    #     number_of_rounds = input('How many rounds do you like to play? ')
    #     if number_of_rounds.isdigit() and int(number_of_rounds) > 0:
    #         number_of_rounds = int(number_of_rounds)
    #         break
    #     else:
    #         print('Invalid input. Please enter a positive number.')
    while True:
        try:
            number_of_rounds = int(input('How many rounds do you like to play? '))
            if number_of_rounds > 0:
                break
            else:
                print('Please enter a positive number.')
        except ValueError:
            print('Invalid input. Please enter a positive number.')
            continue
    user_player = HumanPlayer(number_of_rounds)
    computer_player = ComputerPlayer()
    game1 = Game(user_player, computer_player)
    game1.play()
    game1.summary()

if __name__ == '__main__':
    main()
    