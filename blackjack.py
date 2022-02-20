import random

playerIn = True
dealerIn = True

#create deck
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'K', 'Q', 'J',
        2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'K', 'Q', 'J',
        2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'K', 'Q', 'J',
        2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'K', 'Q', 'J']
playerHand = []
dealerHand = []

#distribute cards
def dealCards(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)

#print hand

#hand count
def total(turn):
    total = 0
    face = ['K', 'Q', 'J']
    for card in turn:
        if (card in range(1, 11)):
            total += card
        elif card in face:
            total += 10
        else:
            if (total + 11 > 21):
                total += 1
            else:
                total += 11
    return total

#show dealer hand
def revealDealerHand(): 
    if len(dealerHand) == 2:
        return dealerHand[1]
    elif len(dealerHand) > 2:
        return dealerHand[0], dealerHand[1]

#game loop
for _ in range(2):
    dealCards(playerHand)
    dealCards(dealerHand)

while playerIn or dealerIn:
    print(f'Dealer showing: {revealDealerHand()}, ?')
    print(f'Player has {playerHand}, Total: {total(playerHand)}')

    if total(playerHand) == 21:
        playerIn = False
        print("PLAYER HAS BLACKJACK!\nPLAYER WINS!")
    elif total(dealerHand) == 21:
        dealerIn = False
        print("Dealer has blackjack.\nPLAYER LOSES!")
    else:
        if playerIn:
            stayOrHit = input("(1) Hit\n(2) Stand\n")
            if stayOrHit == '2':
                playerIn = False
            else: 
                dealCards(playerHand)
        if total(dealerHand) > 16:
            dealerIn = False
        else:
            dealCards(dealerHand)
        if total(playerHand) >= 21:
            break
        elif total(dealerHand) >= 21:
            break

if total(playerHand) == 21:
    print(f"\nDealer Hand: {dealerHand} Total: {total(dealerHand)}\nPlayer Hand: {playerHand} Total: {total(playerHand)}")
    print(f"Player has BLACKJACK! PLAYER WINS")
elif total(dealerHand) == 21:
    print(f"\nDealer Hand: {dealerHand} Total: {total(dealerHand)}\nPlayer Hand: {playerHand} Total: {total(playerHand)}")
    print(f"\nDealer has blackjack. PLAYER LOSES!")
elif total(playerHand) > 21:
    print(f"\nDealer Hand: {dealerHand} Total: {total(dealerHand)}\nPlayer Hand: {playerHand} Total: {total(playerHand)}")
    print(f"You BUST! PLAYER LOSES!")
elif total(dealerHand) > 21:
    print(f"\nDealer Hand: {dealerHand} Total: {total(dealerHand)}\nPlayer Hand: {playerHand} Total: {total(playerHand)}")
    print(f"Dealer BUST! PLAYER WINS")
elif 21 - total(dealerHand) < 21 - total(playerHand):
    print(f"\nDealer Hand: {dealerHand} Total: {total(dealerHand)}\nPlayer Hand: {playerHand} Total: {total(playerHand)}")
    print(f"PLAYER LOSES!")
elif 21 - total(dealerHand) > 21 - total(playerHand):
    print(f"\nDealer Hand: {dealerHand} Total: {total(dealerHand)}\nPlayer Hand: {playerHand} Total: {total(playerHand)}")
    print(f"PLAYER WINS!")




# print(dealerHand)
# print(playerHand)


#player(s) hand

#player(s) blackjack

#hit

#stand

#player score

#dealer score

#push

#win

#lose
#number of decks


