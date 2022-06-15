import random

#empty list used to track cards drawn to avoid duplicate cards.
cards_drawn = []
# this function is to generate a random card.
def draw_card():
    # Card components
    #suits = "♠️♣️♥️♦️" - not currently using this but I've left it in because I hope to replace the suit words with the suite emoji.
    suits = ['Spade', 'Heart', 'Club', 'Diamond']
    card_names = ['A', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    # "shuffling" a card
    draw_a_suit = suits[random.randint(0, len(suits)-1)]
    draw_a_name = card_names[random.randint(0, len(card_names)-1)]

    #combined values to make the card
    new_card = f"{draw_a_name}-{draw_a_suit}"
    return new_card

# print(f"Computer drew, {draw_card()}")


# this function asks the user how many cards they need and keeps pulling until it has a unique list equalling the requested number.
def card_deck():
    hand = input("How many cards would you like?: ")
    #empty variable for the future hand
    card_hand = ""
    #list to confirm if a card has been drawn or not
    count = 1
    while count <= int(hand):
        temp_card = draw_card()
        if temp_card not in cards_drawn:
            cards_drawn.append(temp_card)
            card_hand += temp_card
            card_hand += "\n"
            count += 1

    return card_hand

print(card_deck())
# print(cards_drawn)

#just realized I deleted all the stuff that checks to make sure user is inputing a positive number.
