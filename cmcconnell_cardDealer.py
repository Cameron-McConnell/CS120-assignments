import random

# Constants
NUMCARDS = 52
RANKNAME = (
    "Ace", "Two", "Three", "Four", "Five", "Six", "Seven",
    "Eight", "Nine", "Ten", "Jack", "Queen", "King"
)
SUITNAME = ("Clubs", "Diamonds", "Hearts", "Spades")
DECK = 0
PLAYER = 1
COMPUTER = 2

# initCard()
def initCards():
    cardDB = [DECK] * NUMCARDS
    return cardDB

# assignCard()
def assignCard(cardDB, hand):
    assigned = False
    while not assigned:
        cardNum = random.randrange(NUMCARDS)
        if cardDB[cardNum] == DECK:
            cardDB[cardNum] = hand
            assigned = True

# getCardName()
def getCardName(cardNum):
    suit = cardNum // 13
    rank = cardNum % 13
    cardName = f"{RANKNAME[rank]} of {SUITNAME[suit]}"
    return cardName

# showDB()
def showDB(cardDB):
    print("=== Full Deck Status ===")
    for cardNum in range(NUMCARDS):
        cardName = getCardName(cardNum)
        if cardDB[cardNum] == DECK:
            locName = "Deck"
        elif cardDB[cardNum] == PLAYER:
            locName = "Player"
        elif cardDB[cardNum] == COMPUTER:
            locName = "Computer"
        else:
            locName = f"Unknown({cardDB[cardNum]})"
        print(f"{cardNum}: {cardName} - {locName}")
    print()  # Add blank line after full deck

# showHand()
def showHand(cardDB, hand):
    if hand == PLAYER:
        print("=== Player's Hand ===")
    elif hand == COMPUTER:
        print("=== Computer's Hand ===")

    for cardNum in range(NUMCARDS):
        if cardDB[cardNum] == hand:
            print(f"  {getCardName(cardNum)}")
    print()  # Add blank line after hand

# main
def main():
    cardDB = initCards()
    for _ in range(5):
        assignCard(cardDB, PLAYER)
        assignCard(cardDB, COMPUTER)

    showDB(cardDB)
    showHand(cardDB, PLAYER)
    showHand(cardDB, COMPUTER)

# Run program
if __name__ == "__main__":
    main()
