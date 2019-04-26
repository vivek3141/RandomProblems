'''
Created on Jan 16, 2019

@author: mark_kwong
'''

#===========================================================================
# Description: a single standard card
#
# State Attributes
#   rank - string character 2 to 10 or A, J, Q, K
#   suit - string character h, d, s, c (for heart, diamond, spade or club)
# Methods
#   getValue() - returns an integer from 1-13 depending on the rank of the card
#   __str__() - returns a string like '4d' for 4 of diamonds
#===========================================================================
class Card:
    
    SUIT = ['h', 'd', 's', 'c']
    RANK = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        
    # Returns a numerical value for cards 1-13 depending on the rank of the card
    def getValue(self):
        if self.rank == 'A':
            return(1)
        elif self.rank == 'J':
            return(11)
        elif self.rank == 'Q':
            return(12)
        elif self.rank == 'K':
            return(13)
        elif self.rank in '23456789' or self.rank == '10':
            return(int(self.rank))
        else:
            raise ValueError('{} is of unkwown value'.format(self.rank))
       
    def __str__(self):
        return('{}{}'.format(self.rank, self.suit)) 
