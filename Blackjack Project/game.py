'''
Created on Feb 6, 2019

@author: 
'''
from card import Card
from cards import Cards
from player import Player
import random


# make a BlackjackCard Class inherit from Card
class BlackjackCard(Card):
    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

    def getValue(self):
        if self.rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10']:
            return int(self.rank)
        if self.rank == ['A']:
            return 11
        else:
            return 10


# make a BlackjackHand Class
class BlackjackHand(Cards):
    def getTotalWithAce(self):
        total = 0
        for card in self.cards:
            total = total + card.getValue()
        if total > 21 and 'A' in self.cards:
            total = total - 10  # if the total with ace  = 11 is greater than 21, then ace will equal 1(subtract 10 from total)
        return total

    def bust(self):
        return self.getTotalWithAce() > 21


# make a BlackjackPlayer Class
class BlackjackPlayer(Player):
    def __init__(self, name, amount):
        super().__init__(name, amount)
        self.hand = BlackjackHand()

    def tossHand(self):
        self.hand = BlackjackHand()

    def askHit(self):
        hit = input("Hit? y/n: ")  # ask if they want a hit
        if hit == "y":
            return True
        elif hit == "n":
            return False


# make a BlackjackDealer Class +
class BlackjackDealer(Player):
    def __init__(self, name, amount):
        self.name = name
        self.money = amount
        self.hand = BlackjackHand()  # initialize with an empty hand of cards, but with class BlackjackHand
        # returns False if dealer busts, and True means hit

    def askHit(self):
        if self.hand.getTotalWithAce() >= 21:
            # False represents no hit
            return False
        if self.hand.getTotalWithAce() < 17:  # because the dealer has to hit when his hand is less than 17
            # True represents hit
            return True


def blackjackGame():
    print("Welcome to BlackJack")
    name = input("What is your name: ")
    amount = input("How many games would you like to play: ")
    playerwins = 0
    dealerwins = 0
    gameO = False
    hit = True
    dhit = False
    # make the 2 players

    # make a deck of card
    deck = Cards()  # make empty deck
    deck.shuffle()
    # add the 52-cards and shuffle
    for SUIT in ['h', 'd', 's', 'c']:
        for RANK in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
            deck.add(BlackjackCard(RANK, SUIT))
    deck.shuffle()

    dealer = BlackjackDealer("Dealer", 1)
    player = BlackjackPlayer(name, 1)

    def pprint():
        print()
        print("dealers hand:" + str(dealer.hand.getTotalWithAce()))
        print("player's hand:" + str(player.hand.getTotalWithAce()))
        print()
        print("Player Wins {}".format(playerwins))
        print("Dealer Wins {}".format(dealerwins))
        print()

    for i in range(int(amount)):
        check = True
        player.hand = BlackjackHand()
        dealer.hand = BlackjackHand()
        player.hand.add(deck.deal())
        player.hand.add(deck.deal())
        dealer.hand.add(deck.deal())
        dealer.hand.add(deck.deal())
        print("*" * 10)
        print("Round {}".format(i))
        print("*" * 10)
        print(player)
        print("This is the dealers Hand:[{} Unkown]".format(dealer.hand.cards[0]))
        if player.hand.getTotalWithAce() == 21:
            if dealer.hand.getTotalWithAce() != 21:
                print("player Wins!")
                playerwins += 1
                pprint()
                check = False
                continue
            if dealer.hand.getTotalWithAce() == 21:
                print("Tie!")
                dealerwins += 1
                playerwins += 1
                pprint()
                check = False
                continue
        if dealer.hand.getTotalWithAce() == 21:
            if player.hand.getTotalWithAce() != 21:
                print("dealer wins")
                dealerwins += 1
                pprint()
                check = False
                continue

        hit = True
        while hit:
            hit = player.askHit()
            if hit:
                player.hand.add(deck.cards.pop())
            if player.hand.getTotalWithAce() > 21:
                print("Player busts")
                dealerwins += 1
                pprint()
                check = False
                hit = True
                break

        if not hit:
            while dealer.askHit():
                dealer.hand.add(deck.cards.pop())
                if dealer.hand.getTotalWithAce() > 21:
                    print("dealer busts, You Win!")
                    playerwins += 1
                    pprint()
                    check = False
                    break

        if check:
            if dealer.hand.getTotalWithAce() > player.hand.getTotalWithAce():
                print("dealer wins")
                dealerwins += 1
            if dealer.hand.getTotalWithAce() < player.hand.getTotalWithAce():
                print("Player Wins!")
                playerwins += 1
            if dealer.hand.getTotalWithAce() == player.hand.getTotalWithAce():
                print("Tie!")
                dealerwins += 1
                playerwins += 1
            pprint()
    print("\n" * 3)
    print("*" * 10)
    print("Game Over")
    print("Player Wins {}".format(playerwins))
    print("Dealer Wins {}".format(dealerwins))
    print("*" * 10)


blackjackGame()
