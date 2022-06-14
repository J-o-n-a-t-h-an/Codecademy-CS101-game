import random

def card_draw():
    hand = input("How many cards would you like?: ")
    #empty variable for the future hand
    card_hand = ""
    #list to confirm if a card has been drawn or not
    cards_drawn = []
    if hand.isnumeric():
        for i in range(0, int(hand)):
            # Card components
            #suits = "♠️♣️♥️♦️" - not currently using but left in.  Hoping to make the cards "graphic" instead of the name sometime in the future.
            suits = ['Spade', 'Heart', 'Club', 'Diamond']
            card_names = ['A', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

            # "shuffling" a card
            draw_a_suit = suits[random.randint(0, len(suits)-1)]
            draw_a_name = card_names[random.randint(0, len(card_names)-1)]

            #combined values to make a card
            new_card = f"{draw_a_name}-{draw_a_suit}"

            #storing card information
            if len(cards_drawn) == 0:
                cards_drawn.append(new_card)
            else:
                for i in range(0, int(hand)):
                    if cards_drawn[i] == new_card:
                        break
                    else:
                        cards_drawn.append(new_card)
                        card_hand += new_card
                        card_hand += "\n"
        print(card_hand)
        print(cards_drawn)
    else:
        return f"Sorry but {str(hand)} is not an appropriate answer.  Please select a number greater than zero."

print(card_draw())
