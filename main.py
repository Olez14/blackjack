import random

# Old Version
#cards = [[1, 1],[2, 2],[3, 3],[4, 4],[5, 5],[6, 6],[7, 7],[8, 8], [9,9],[10, 10],["J", 10],["K", 10],["Q", 10],["A"]]

cards = {
    # card: points
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    10: 10,
    "J": 10,
    "K": 10,
    "Q": 10,
    "A": "A",
}
playerCards = []
dealerCards = []

def getCardsAsString(cardsTable):
    string = ""
    for card in cardsTable:
        string = string + str(card) + ", "
    return string

def getDealerCardsAsString(cardsTable):
    string = ""
    index = 1
    for card in cardsTable:
        if index == 1:
            string = string + "???" + ", "
        else:
            string = string + str(card) + ", "
        index += 1
    return string

def getPlayerScore(cardsTable):
    score = 0
    for card in cardsTable:
        if card == "A":
            if score + 11 > 21:
                score += 1
            else:
                score += 11
        else:
            score += cards[card]
    return score

def processDealerCard():
    if not isDealerShouldStop():                # Zakładamy, że krupier przy około 16 ma szansę jeszcze na wygraną
        addPlayerRandomCard(dealerCards)
        print("Karty krupiera: ", getDealerCardsAsString(dealerCards))
        return True
    else:
        return False

def isDealerShouldStop():
    if getPlayerScore(dealerCards) <= 16:                # Zakładamy, że krupier przy około 16 ma szansę jeszcze na wygraną
        return False
    else:
        return True

def addPlayerRandomCard(playerCards):
    keysOfCards = list(cards.keys())
    randomCard = random.randint(0, len(keysOfCards) - 1)
    playerCards.append(keysOfCards[randomCard])

# Losowanie 2 kart dla gracza i krupiera
addPlayerRandomCard(playerCards)
addPlayerRandomCard(playerCards)

addPlayerRandomCard(dealerCards)
addPlayerRandomCard(dealerCards)

print("Twoje karty: ",getCardsAsString(playerCards), "Lacznie:", getPlayerScore(playerCards))
print("Karty krupiera: ",getDealerCardsAsString(dealerCards))

while(getPlayerScore(playerCards)<21 or not isDealerShouldStop()):
    playerChoise = input("Dobierz kartę[1] lub pozostań[2]... ")
    if playerChoise == "1":
        addPlayerRandomCard(playerCards)
        print("Twoje karty: ", getCardsAsString(playerCards), "Lacznie:", getPlayerScore(playerCards))
        processDealerCard()
    else:
        while(not isDealerShouldStop()):
            processDealerCard()
        break

print("Karty krupiera:",getCardsAsString(dealerCards), "Lacznie:", getPlayerScore(dealerCards))


if getPlayerScore(playerCards) == getPlayerScore(dealerCards):
    print("Remis! Nikt nie wygrał!")
    exit()
if (getPlayerScore(playerCards) > getPlayerScore(dealerCards) and getPlayerScore(playerCards) <= 21 and getPlayerScore(dealerCards) <= 21):
     print("Wygrałes!")
     exit()
if getPlayerScore(playerCards) < getPlayerScore(dealerCards) and getPlayerScore(playerCards) > 21 and getPlayerScore(dealerCards) > 21:
     print("Wygrałes!")
     exit()
if getPlayerScore(dealerCards) > 21 and  getPlayerScore(playerCards) <= 21:
    print("Wygrałes!")
    exit()
print("Przegałeś... Krupier wygrał")
exit()
