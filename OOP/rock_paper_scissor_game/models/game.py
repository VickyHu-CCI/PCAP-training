
class Game():
    rules = {
        ('r','r'): 'tie',
        ('r','p'): 'lost',
        ('r','s'): 'won',
        ('p','r'): 'won',
        ('p','p'): 'tie',
        ('p','s'): 'lost',
        ('s','r'): 'lost',
        ('s','p'): 'won',
        ('s','s'): 'tie'
    }
    def __init__(self, player1, player2) -> None:
        '''
        The player1 is the user and player2 is the computer.
        '''
        self.__player1 = player1
        self.__player2 = player2
        self.__round_count = 1

    def play(self) -> None:
        while self.__round_count <= self.__player1.get_plan_rounds:
            print(f'---- Round {self.__round_count} ----')
            user_output = self.__player1.move()
            pc_output = self.__player2.move()
            print(f'You: {user_output} | Computer: {pc_output}')
            try:
                result = Game.rules[(user_output, pc_output)]
            except KeyError:
                print("Invalid move detected. Please ensure valid inputs and rules.")
                continue
            if result == 'won':
                print(f'You {result} this round!')
                print('\n')
                self.__player1.increse_score(1)
            elif result == 'lost':
                print(f'You {result} this round!')
                print('\n')
                self.__player2.increse_score(1)
            else:
                print(f'This round is a {result}!')
                print('\n')
            self.__round_count += 1

    def summary(self) -> None:
        print(f'[Game Summary] Your points {self.__player1.get_score} | Computer points {self.__player2.get_score}')
        if self.__player1.get_score > self.__player2.get_score:
            print('You won.')
        elif self.__player1.get_score < self.__player2.get_score:
            print('Computer won.')
        else:
            print('It was a tie.')
        





