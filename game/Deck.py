#Manages the deck of 52 cards
from Card import Card
import random

class Deck():
    def __init__(self):
        ranks = Card.RANKS
        suits = Card.SUITS
        deck = []#datatype is an array

        for rank in ranks:
            for suit in suits:
                card = Card(suit=suit,rank=rank)
                deck.append(card)
        self.deck = deck

    def shuffle(self):
        newDeck = []
        deck = self.deck
        
        while (True):
            if len(deck) == 1:
                card =  deck[0]
                newDeck.append(card)
                break
            n = random.randint(0 ,len(deck)-1)
            card=deck[n]
            deck.pop(n)
            newDeck.append(card)
        
        self.deck = newDeck
        
    def burn_card(self):
        #take the top card and put it below
        if len(self.deck) == 0:
            print("Deck is empty, cannot burn card.")
            return None
        
        burned = self.deck.pop(0)
        print(f"Burned card: {burned}")
        return burned

    def give_card(self):
        #deals the top card
        if len(self.deck) == 0:
            print("Deck is empty, no cards to give.")
            return None
        return self.deck.pop(0)

if __name__=="__main__":
    d1 = Deck()

    print("Before shuffle:")
    print(d1.deck)

    d1.shuffle()

    print("\nAfter shuffle:")
    print(d1.deck)

    print("\nBurning a card:")
d1.burn_card()

print("\nGiving 3 cards:")
for _ in range(3):
    print(d1.give_card())

print("\nRemaining deck:")
print(d1.deck)