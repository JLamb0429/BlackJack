#! python3
# Assignment topic 4-1
# Programmer Name: Joshua Lamb
# Project name: BlackJack
# Created: 7/12/2018
# Updated: 7/15/2018
# Playing cards 1.0 Use object oriented programing to craft a black jack game.


from random import randint
from time import sleep

class Deck():
    """Deck builds a 52 item dictionary of cards and score values"""
    def __init__(self):
        self.suits = ("Hearts", "Spades", "Diamonds", "Clubs")
        self.ranks = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King")
        self.cardScores = (11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10)
        self.deck_scores = {}
        self.deck = []


    def assembleDeck(self):
        '''assemble deck takes each suit value in the suit tuple and applies all 13 ranks and adds them
        to a new dictionary.
         example 1: key = suit_rank:value = score...
         example 2: key = Ace_Spades: score = 11'''

        for i in range(4):
            s = str(self.suits[i])
            for j in range(13):
                r = self.ranks[j]  # is my key error, need to figure method to choose keys by order
                c = self.cardScores[j]
                self.deck.append(s + '_' + r)
                self.deck_scores.setdefault(s + '_' + r, c)


    def addCard(self):
        """ Allow Child classes to draw from the deck, after drawing from the deck that card value is deleted from the
        card_Deck.deck list so that it cannot be selected twice"""

        self.card_draw = str(card_Deck.deck[randint(0,len(card_Deck.deck)-1)])
        self.card_rank1 = self.card_draw #"Key of self.card_draw1"
        return self.card_rank1
        card_Deck.deck.remove(self.card_draw)


class Dealer_Hand(Deck):
    # This classes inherit from the Deck class
    global card_Deck
    ''' Craft the dealers hand and score'''
    def __init__(self):
        #Card 1 rank and score
        self.card1_rank = self.addCard()
        self.card1_score = card_Deck.deck_scores[self.card1_rank]

        # Card 2 rank and score
        self.card2_rank = self.addCard()
        self.card2_score = card_Deck.deck_scores[self.card2_rank]

        self.score = (self.card1_score + self.card2_score)


class Player_Hand(Deck):
    #This classes inherit from the Deck class
    global card_Deck
    ''' Craft the players hand and score'''
    def __init__(self):
        # Card 1 rank and score
        self.card1_rank = self.addCard()
        self.card1_score = card_Deck.deck_scores[self.card1_rank]

        # Card 2 rank and score
        self.card2_rank = self.addCard()
        self.card2_score = card_Deck.deck_scores[self.card2_rank]

        self.score = (self.card1_score + self.card2_score)

    def hitMe(self):
        global dealerHand, card_Deck, playerHand #dealer.card1_rank, dealer.card2_rank, dealer.score
        print(dealerHand)
        print(playerHand)
        playerHit = input("Press \"H\" to hit. Any key to call.")
        playerDraw = True
        while playerHit.upper() == "H" and playerDraw == True:
            print ("Something")

            if playerHit.upper() == "H":
                # Third Card Drawn
                self.card3_rank = self.addCard()
                self.card3_score = card_Deck.deck_scores[self.card3_rank]
                self.score = (self.score + self.card3_score)
                if self.score < 21:
                    #Draw a card and and show the value as long as the player score is less than 21.
                    playerDraw -= 1
                    playerHand = ("You have %s, %s, %s, a score of %2d" % (player.card1_rank, player.card2_rank, player.card3_rank, player.score))
                    print(dealerHand)
                    print(playerHand)
                    playerHit = input("Press \"H\" to hit. Any key to call.")
                else:
                    # If the player score is more than 21 print
                    playerHand = ("Bust You have %s, %s, %s, a score of %2d" % (player.card1_rank, player.card2_rank, player.card3_rank, player.score))
                    dealerHand = ("The Dealer Has %s and %s a score of %d" %(dealer.card1_rank, dealer.card2_rank, dealer.score))
                    print(dealerHand)
                    print(playerHand)
                    playerDraw = False
            else:
                playerDraw = False

            if playerHit.upper() == "H":
                # Fourth Card Drawn
                self.card4_rank = self.addCard()
                self.card4_score = card_Deck.deck_scores[self.card4_rank]
                self.score = (self.score + self.card4_score)
                if self.score < 21:
                    #Draw a card and and show the value as long as the player score is less than 21.
                    playerDraw -= 1
                    playerHand = ("You have %s, %s, %s, %s, a score of %2d" % (player.card1_rank, player.card2_rank, player.card3_rank, player.card4_rank, player.score))
                    print(dealerHand)
                    print(playerHand)
                    playerHit = input("Press \"H\" to hit. Any key to call.")
                else:
                    # If the player score is more than 21 print
                    playerHand = ("Bust You have %s, %s, %s, %s, a score of %2d" % (player.card1_rank, player.card2_rank, player.card3_rank, player.card4_rank, player.score))
                    dealerHand = ("The Dealer Has %s and %s a score of %d" %(dealer.card1_rank, dealer.card2_rank, dealer.score))
                    print(dealerHand)
                    print(playerHand)
                    playerDraw = False
            else:
                playerDraw = False

            if playerHit.upper() == "H":
                # Fifth Card Drawn
                self.card5_rank = self.addCard()
                self.card5_score = card_Deck.deck_scores[self.card5_rank]
                self.score = (self.score + self.card5_score)
                if self.score < 21:
                    #Draw a card and and show the value as long as the player score is less than 21.
                    playerDraw -= 1
                    playerHand = ("You have %s, %s, %s, %s, %s, a score of %2d" % (player.card1_rank, player.card2_rank, player.card3_rank, player.card4_rank, player.card5_rank, player.score))
                    print(dealerHand)
                    print(playerHand)
                    playerHit = input("Press \"H\" to hit. Any key to call.")
                else:
                    # If the player score is more than 21 print
                    playerHand = ("Bust You have %s, %s, %s, %s, %s a score of %2d" % (player.card1_rank, player.card2_rank, player.card3_rank, player.card4_rank, player.card5_rank, player.score))
                    dealerHand = ("The Dealer Has %s and %s a score of %d" %(dealer.card1_rank, dealer.card2_rank, dealer.score))
                    print(dealerHand)
                    print(playerHand)
                    playerDraw = False
            else:
                playerDraw = False

            if playerHit.upper() == "H":
                # Sixth Card Drawn
                self.card6_rank = self.addCard()
                self.card6_score = card_Deck.deck_scores[self.card6_rank]
                self.score = (self.score + self.card6_score)
                if self.score < 21:
                    #Draw a card and and show the value as long as the player score is less than 21.
                    playerDraw -= 1
                    playerHand = ("You have %s, %s, %s, %s, %s, %s  a score of %2d" % (player.card1_rank, player.card2_rank, player.card3_rank, player.card4_rank, player.card5_rank, player.card6_rank, player.score))
                    print(dealerHand)
                    print(playerHand)
                    playerHit = input("Press \"H\" to hit. Any key to call.")
                else:
                    # If the player score is more than 21 print
                    playerHand = ("Bust You have %s, %s, %s, %s, %s, %s a score of %2d" % (player.card1_rank, player.card2_rank, player.card3_rank, player.card4_rank, player.card5_rank, player.card6_rank, player.score))
                    dealerHand = ("The Dealer Has %s and %s a score of %d" %(dealer.card1_rank, dealer.card2_rank, dealer.score))
                    print(dealerHand)
                    print(playerHand)
                    playerDraw = False
            else:
                playerDraw = False

            if playerHit.upper() == "H":
                # Seventh Card Drawn
                self.card7_rank = self.addCard()
                self.card7_score = card_Deck.deck_scores[self.card7_rank]
                self.score = (self.score + self.card7_score)
                if self.score < 21:
                    #Draw a card and and show the value as long as the player score is less than 21.
                    playerDraw -= 1
                    playerHand = ("You have %s, %s, %s, %s, %s, %s, %s  a score of %2d" % (player.card1_rank, player.card2_rank, player.card3_rank, player.card4_rank, player.card5_rank, player.card6_rank, player.card7_rank, player.score))
                    print(dealerHand)
                    print(playerHand)
                    playerHit = "C"
                else:
                    # If the player score is more than 21 print
                    playerHand = ("Bust You have %s, %s, %s, %s, %s, %s, %s a score of %2d" % (player.card1_rank, player.card2_rank, player.card3_rank, player.card4_rank, player.card5_rank, player.card6_rank, player.card7_rank, player.score))
                    dealerHand = ("The Dealer Has %s and %s a score of %d" %(dealer.card1_rank, dealer.card2_rank, dealer.score))
                    print(dealerHand)
                    print (playerHand)
                    playerDraw = False
            else:
                playerDraw = False
            playerDraw = False



def call(dealerScore1, playerScore1):
    #Evaluate dealer and player scores Display the winner
    if dealerScore1 >= playerScore1:
        print ("Dealer score is %d, your score is %d" % (dealerScore1, playerScore1))
        print ("House Wins")
    elif playerScore1 > 21:
        print ("Bust. House wins")
    elif playerScore1 > dealerScore1 and playerScore1 < 21:
        print ("Dealer score is %d, your score is %d" % (dealerScore1, playerScore1))
        print ("You win!")



""" Main function starts the Game"""
# card_Desk assembly
card_Deck = Deck()
card_Deck.assembleDeck()

dealer = Dealer_Hand()
dealerHand = ("Dealer has %s showing a score of %2d" % (dealer.card1_rank,dealer.card1_score))
player = Player_Hand()
playerHand = ("You have %s and %s a score of %2d" % (player.card1_rank, player.card2_rank, player.score))

player.hitMe()

call (dealer.score, player.score)

sleep(30)

