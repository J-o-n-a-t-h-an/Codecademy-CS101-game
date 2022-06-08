from datetime import datetime

#date and time stuff
now = datetime.now()
#time_format = "%Y/%m/%d - %H:%M:%S"
time_format = "%Y/%m/%d"
time_now = now.strftime(time_format)

# User questions/interactions and testing
print(f"Welcome to MadLibs!")
user_name = input("Hello! What is your name? \n")
#print(time_now)
print("You will be asked for some words and phrases to insert into your madlib.")
chosen_theme = input(f"{user_name}, please choose a theme.\n")
chosen_place = input(f"Please choose a location.\n")
chosen_day = input(f"Choose a day of the week.\n")
chosen_time = input(f"Please choose a time.\n")
chosen_verb = input(f"please choose a verb.\n")
chosen_animal = input(f"please choose an animal.\n")
chosen_body = input(f"please select a body part.\n")
contact = input(f"Finally, we need some contact information.\n")

name = user_name
theme = chosen_theme
place = chosen_place
day_of_week = chosen_day
time = chosen_time
verb = chosen_verb
animal = chosen_animal
body_part = chosen_body
contact_information = contact

mad_libs_01 = f"""
{name} is having a {theme} party!
It's going to be at {place} on {day_of_week}.
Please make sure to show up at {time}, or else you will be required to {verb} a/an {animal} with your {body_part}.
RSVP at {contact_information}.
"""

print(mad_libs_01)