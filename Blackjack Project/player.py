'''
Created on Jan 17, 2019

@author: mark_kwong
'''
import cards


# ===========================================================================
# Description: a card player with money and a hand of cards
#
# State Attributes
#    name - string - the name of the player
#    hand - Cards - a bunch of cards
#    money - integer - how much money player has
# Methods
#    introduce() - prints out message "Hi, my name is ..."
#    __str__() - returns a string ex. 'Joe: [4d 7c 10s Ah]'
#    addCard(card) - add card to the player's hand of cards
#    tossHand() - throw away the hand of cards and start with a new empty card hand
#    addMoney(amt) - add amt to player's money
# ===========================================================================
class Player:

    # inputs:
    #    name - string for the player's name
    #    amount - integer for how much money the player has
    def __init__(self, name, amount):
        '''
        Constructor
        '''
        self.name = name
        self.money = amount
        self.hand = cards.Cards()  # initialize with an empty hand of cards

    # prints out name and the hand of cards    
    def __str__(self):
        return ("{}: {}".format(self.name, self.hand))

    def introduce(self):
        print("Hi, my name is {}".format(self.name))

    # add (or subtract) player's money    
    def addMoney(self, amount):
        self.money += amount

    # when player given another card, add it it player's hand    
    def addCard(self, card):
        self.hand.add(card)

    # when done with a round, toss cards and start with a new empty hand of cards
    def tossHand(self):
        self.hand = cards.Cards()
