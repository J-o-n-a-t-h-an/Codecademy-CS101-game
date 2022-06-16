from datetime import datetime

print(f"Welcome to MadLibs!")
print(f"I'm excited to be making a MadLib with you today.")
user_name = input(f"What is your name?\n")
i_dont_care = input(f"How is your day going today?\n")
print(f"Sorry to hear that but I don't really care.")
print(f"Please select a MadLib to write.\n")
print(f"Party, Vacation, Excused, Hall Pass")
choice_counter = 0
while choice_counter == 0:
    madlib_choice = input(f"which Madlib would you like to do?\t")
    # the following print statements have been used to test that my while/if stuff is working correctly.  Ultimately i'll remove them and put in more appropriate code.
    if madlib_choice.lower() == "party":
        print(f"Lets {madlib_choice}")
        break
    elif madlib_choice.lower() == "vacation":
        print(f"Lets {madlib_choice}")
        break
    elif madlib_choice.lower() == "excused":
        print(f"Lets {madlib_choice}")
        break
    elif madlib_choice.lower() == "hall pass":
        print(f"Lets {madlib_choice}")
        break
    else:
        print(f"Your choice of: {madlib_choice} doesn't match one of the options or is spelled incorrectly, please select again.")

print(f"""
\n
\n
\n
\n
\n
\n
""")



class MadLib:
    """
    Documentation?
    """
    #date and time stuff
    time_now = datetime.now()
    #time_format = "%Y/%m/%d - %H:%M:%S"
    time_format = "%Y/%m/%d"
    time_now_formatted = time_now.strftime(time_format)

    def __init__(self):
        pass
    # Party Madlib
    def party(self):
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
        This MadLib was created by {user_name} on {time_now_formatted}.
        """













# Old stuff until I get everything working
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

"""
#date and time stuff
time_now = datetime.now()
#time_format = "%Y/%m/%d - %H:%M:%S"
time_format = "%Y/%m/%d"
time_now_formatted = time_now.strftime(time_format)

"""