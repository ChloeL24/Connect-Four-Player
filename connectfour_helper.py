

from ps9pr1 import Board

# write your class below.

class Player:
    '''a data type that represents a player of the connect four game'''

    
    def __init__(self,checker):
        '''constructs a new player object and keeps track of the number of moves'''
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0
    
    def __repr__(self):
        '''returns a string representing the player object'''
        if self.checker == 'X':
            return 'Player X'
        if self.checker == 'O':
            return 'Player O'
        
    def opponent_checker(self):
        '''returns a string representing the checker of the Player object's opponent'''
        if self.checker == 'X':
            return 'O'
        if self.checker == 'O':
            return 'X'
        
    def next_move(self, b):
        '''accepts a Board object b as a parameter and returns the column where 
        the player wants to make the next move'''
        self.num_moves += 1
        while True:
            column = int(input('Enter a column: '))
            if b.can_add_to(column) == True:
                return column
                self.num_moves += 1
            else:
                print('Try again!')