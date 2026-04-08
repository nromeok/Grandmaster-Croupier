#Represents a single playing card

class Card ():
    RANKS = ["K","Q","J","10","9","8","7","6","5","4","3","2","A"]
    SUITS = ["HEART","DIAMOND", "SPADE","CLUB"]

    def __init__(self,suit,rank):
        
        if not isinstance(suit, str):
            raise TypeError(f"Suite expected to be a string got {type(suit).__name__}")
        if not isinstance(rank,str):
            raise TypeError(f"Rank expected to be a string got {type(rank).__name__}")
        
        suitUpper = suit.upper()
        rankUpper = rank.upper()

        if suitUpper in Card.SUITS:
            pass
        else:
            raise TypeError(f"Added suit not in {Card.SUITS}")
        
        if rankUpper in Card.RANKS:
            pass
        else:
            raise TypeError(f"Added rank not in {Card.RANKS}")
        
        self.rank = rankUpper
        self.suit = suitUpper

    def __repr__(self):
        suit_symbols = {
            "HEART": "♥",
            "DIAMOND": "♦",
            "SPADE": "♠",
            "CLUB": "♣"
        }
        return f"{self.rank}{suit_symbols[self.suit]}"
    
    def __str__(self):
        return self.__repr__()
    
    def printCard(self):
        print(f"Rank: {self.rank}, Suit: {self.suit}")
if __name__ == "__main__":
    # card1 = Card(suit = "Joker", rank = "A")
    # card1.printCard()

    card2 = Card(suit = "Heart", rank = "4")
    card2.printCard()
        