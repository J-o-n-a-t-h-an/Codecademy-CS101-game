from datetime import datetime

#date and time stuff
now = datetime.now()
#time_format = "%Y/%m/%d - %H:%M:%S"
time_format = "%Y/%m/%d"
time_now = now.strftime(time_format)
"""
# User questions/interactions and testing
print(f"Welcome to MadLibs!")
user_name = input("Hello! What is your name? \n")
#print(time_now)
print("You will be asked for some words and phrases to insert into your madlib.")
theme = input(f"{user_name}, please choose a theme.\n")
place = input(f"Please choose a location.\n")
day_of_week = input(f"Choose a day of the week.\n")
chosen_time = input(f"Please choose a time.\n")
verb = input(f"please choose a verb.\n")
animal = input(f"please choose an animal.\n")
body_part = input(f"please select a body part.\n")
contact_information = input(f"Finally, we need some contact information.\n")
"""

'''
mad_libs_01 = f"""
{user_name} is having a {theme} party!
It's going to be at {place} on {day_of_week}.
Please make sure to show up at {chosen_time}, or else you will be required to {verb} a/an {animal} with your {body_part}.
RSVP at {contact_information}.
This MadLib was created by {user_name} on {time_now}.
"""
'''

# print(mad_libs_01)


print(f"Welcome to MadLibs!")
print(f"I'm excited to be making a MadLib with you today.")
user_name = input(f"What is your name?\n")
print(f"Please select a MadLib to write.\n")

print()

class MadLib:
    """
    Documentation?
    """
    #date and time stuff
    now = datetime.now()
    #time_format = "%Y/%m/%d - %H:%M:%S"
    time_format = "%Y/%m/%d"
    time_now = now.strftime(time_format)

    def __init__(self):
        pass

    def party_madlib(self):
        print("You will be asked for some words and phrases to insert into your madlib.")
        theme = input(f"{user_name}, please choose a theme.\n")
        place = input(f"Please choose a location.\n")
        day_of_week = input(f"Choose a day of the week.\n")
        chosen_time = input(f"Please choose a time.\n")
        verb = input(f"please choose a verb.\n")
        animal = input(f"please choose an animal.\n")
        body_part = input(f"please select a body part.\n")
        contact_information = input(f"Finally, we need some contact information.\n")


        mad_libs_01 = f"""
        {user_name} is having a {theme} party!
        It's going to be at {place} on {day_of_week}.
        Please make sure to show up at {chosen_time}, or else you will be required to {verb} a/an {animal} with your {body_part}.
        RSVP at {contact_information}.
        This MadLib was created by {user_name} on {time_now}.
        """

