class Card:
    """A Playing card."""
    RANKS = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    SUITS = ["c","d","h","s"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        reply = self.rank + self.suit
        return reply
    
class Hand:
    """A hand of playing cards."""
    def __init__(self):
        self.cards = []
    
    def __str__(self):
        if self.cards:
            reply = ""
            for card in self.cards:
                reply += str(card) + "  "
        else:
            reply = "<empty>"
        return reply

    def clear(self):
       self.cards = []

    def add(self, card):
      self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)

card1 = Card(rank = "A", suit = "c")
card2 = Card(rank = "2", suit = "c")
card3 = Card(rank = "3", suit = "c")
card4 = Card(rank = "4", suit = "c")
card5 = Card(rank = "5", suit = "c")
print(card1,"\n")
print("Printing the rest of the objects individually")
print(card2)
print(card3)
print(card4)
print(card5)

my_hand = Hand()
print("\nPrinting my hand before I add any cards:\n",my_hand,"\n") #<empty>
print("Printing my hand after adding 5 cards:")
my_hand.add(card1)
my_hand.add(card2)
my_hand.add(card3)
my_hand.add(card4)
my_hand.add(card5)
print(my_hand)

print("\nGave the first two cards from my hand to your hand.")
your_hand = Hand()
my_hand.give(card1, your_hand)
my_hand.give(card2, your_hand)
print("Your hand:")
print(your_hand)
print("My hand:")
print(my_hand,"\n")
my_hand.clear()
print("My hand after clearing it : \n", my_hand)
print("\nPress the enter key to exit.")
