import random

#suits = "♠️♣️♥️♦️"
suits = ['Spade', 'Heart', 'Club', 'Diamond']
suits_random = random.randint(0, len(suits)-1)

#print(suits_random)

draw_a_suit = suits[suits_random]

card_names = ['A', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

draw_a_name = card_names[random.randint(0, len(card_names)-1)]

#drawn_card = draw_a_name+draw_a_suit
drawn_card = f"{draw_a_name}-{draw_a_suit}"
print(drawn_card)

def card_draw():
    # Card components
    #suits = "♠️♣️♥️♦️"
    suits = ['Spade', 'Heart', 'Club', 'Diamond']
    card_names = ['A', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    # "shuffling" a card
    draw_a_suit = suits[random.randint(0, len(suits)-1)]
    draw_a_name = card_names[random.randint(0, len(card_names)-1)]

    return f"{draw_a_name}-{draw_a_suit}"

print(card_draw())

hand = input("How many cards would you like?\n")
card_hand = ""
for i in range(0, int(hand)):
    card_hand += card_draw()
    card_hand += "\n"
print(card_hand)






#these are a test for using inputs within other bits
'''
name = input("Please tell me your name:\n")
print(f"Your name is {name}")
number = input(f"please choose a number {name}\n")
if float(number) > 10:
    animal = input(f"what kind of animal do you like?")
    print(f"{name} likes {animal}")
else:
    color = input(f"What color do you like?")
    print(f"{name} likes {color}")
'''


'''
numero_uno = input("number?\n")
numero_dos = input("number?\n")

def test(one, two):
    print(f"your two numbers are {one}, {two}")
    combined = int(one) * int(two)
    print(f"together they make {combined}")
    question = input(f"would you like to add a third number?\n")
    yes_or_no = ""
    if question == "yes":
        number_three = input("what is your third number?\n")
        final_number = number_three * combined
        return f"Your final number is: {final_number}."
    elif question == "no":
        return f"you chose not to include a new number.  Your final number is: {combined}."
    else:
        return f"Please try again, we need a yes or a no."

print(test(numero_uno, numero_dos))

'''



"""
for i in suits:
    print(i)
for i in card_names:
    print(i)
"""