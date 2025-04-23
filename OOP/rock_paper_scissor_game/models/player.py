from random import choice
from abc import ABC, abstractmethod
class Player(ABC):
    def __init__(self, score: int = 0) -> None:
        self.__score = score

    @abstractmethod
    def move(self):
        '''
        This method should be implemented by subclasses to return the player's move.
        The move can be either 'rock', 'paper', or 'scissors'.
        '''
        pass

    @property
    def get_score(self) -> int:
        '''
        Get the score of user from outside of the class.
        '''
        return self.__score
    
    @get_score.setter
    def get_score(self, score) -> None:
        '''
        Set the score of user from outside of the class.
        '''
        self.__score = score

    def increse_score(self, score: int = 1) -> None:
        '''
        This method should be implemented by subclasses to increase the player's score.
        '''
        self.__score += score

class HumanPlayer(Player):
    def __init__(self, plan_rounds:int = 0) -> None:
        '''
        The plan_rounds is the number of rounds the player wants to play.
        '''
        super().__init__()
        self.__plan_rounds = plan_rounds

    @property
    def get_plan_rounds(self) -> int:
        '''
        Get the plan_rounds of user from outside of the class.
        '''
        return self.__plan_rounds
    
    def move(self) -> str:
        '''
        The move can be either 
        'r' for 'rock', 
        'p' for 'paper', 
        or 's' 'scissors'
        choosed by user player through terminal.
        '''
        user_choice = input("Rock, paper or scissors [r/p/s]?").lower()
        while user_choice not in ['r', 'p', 's']:
            print("Invalid choice. Please try again.")
            user_choice = input("Rock, paper or scissors [r/p/s]?").lower()
        return user_choice



class ComputerPlayer(Player):

    
    def move(self) -> str:
        '''
        The move can be either 'r' for 'rock', 
        'p' for 'paper', 
        or 's' 'scissors'
        randomly choosed by computer.
        '''
        return choice(['r', 'p', 's'])