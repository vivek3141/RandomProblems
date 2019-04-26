'''
Created on Jan 16, 2019

@author: mark_kwong
'''
import random
import card

#===========================================================================
# Description: A list of Card; used for a player's hand or a deck of cards
#
# State Attributes
#     - cards - list of card; starts out empty
# Methods
#     - shuffle() - randomly shuffle all the card in the list
#     - deal() - deal the 'top' card from the hand/deck
#     - add(card) - add card to the list of cards
#     - __str__() - returns string of all the cards in the hand like '[4d 10h As]'
#===========================================================================
class Cards:

    def __init__(self):
        '''
        Constructor
        '''
        self.cards = []
        
    # returns a string of all the cards in the 'deck'
    def __str__(self):
        s = '['
        for card in self.cards:
            if len(s) == 1:
                s = s + str(card)
            else:
                s = s + ' ' + str(card)
        s = s + ']'
        return(s)
    
    # Add card to the 'bottom' of the deck of cards
    def add(self, card):
        self.cards.append(card)
                
    # Deal card from the 'top' of the deck of cards
    def deal(self):
        return self.cards.pop(0)
        
    def shuffle(self):
        random.shuffle(self.cards)
    
        