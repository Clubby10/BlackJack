import random

# Create a deck of cards
deck = []
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
values = {"Ace": 11, "King": 10, "Queen": 10, "Jack": 10, "10": 10,
          "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}

for suit in suits:
    for value in values:
        deck.append(value + " of " + suit)

# Shuffle the deck
random.shuffle(deck)

# Set up the game
player_hand = []
dealer_hand = []

# Deal the cards
for i in range(2):
    player_hand.append(deck.pop())
    dealer_hand.append(deck.pop())

# Helper function to calculate the value of a hand
def hand_value(hand):
    value = 0
    num_aces = 0
    for card in hand:
        card_value = card.split()[0]
        value += values[card_value]
        if card_value == "Ace":
            num_aces += 1
    while value > 21 and num_aces > 0:
        value -= 10
        num_aces -= 1
    return value

# Play the game
while True:
    # Show the player's hand and ask if they want to hit or stand
    print("Player's hand:", player_hand)
    print("Player's hand value:", hand_value(player_hand))
    if hand_value(player_hand) > 21:
        print("Bust! You lose.")
        break
    action = input("Do you want to hit or stand? ")
    if action == "hit":
        player_hand.append(deck.pop())
    elif action == "stand":
        break

# Dealer's turn
while hand_value(dealer_hand) < 17:
    dealer_hand.append(deck.pop())

# Determine the winner
player_hand_value = hand_value(player_hand)
dealer_hand_value = hand_value(dealer_hand)
print("Player's hand:", player_hand)
print("Dealer's hand:", dealer_hand)
print("Dealer's hand value:", dealer_hand_value)
if dealer_hand_value > 21:
    print("Dealer busts! You win!")
elif dealer_hand_value > player_hand_value:
    print("Dealer wins!")
elif player_hand_value > dealer_hand_value:
    print("You win!")
else:
    print("It's a tie.")
