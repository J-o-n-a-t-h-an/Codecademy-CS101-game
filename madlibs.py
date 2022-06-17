from datetime import datetime

# Some of these madlibs were taken from their website at: https://www.madlibs.com/printables/ some of them were created from scratch.

#date and time stuff
time_now = datetime.now()
#time_format = "%Y/%m/%d - %H:%M:%S"
time_format = "%Y/%m/%d"
time_now_formatted = time_now.strftime(time_format)

#Welcome message and madlibs selection.
print(f"Welcome to MadLibs!")
print(f"I'm excited to be making a MadLib with you today.")
user_name = input(f"What is your name? > ")
print(f"Please select a MadLib to write.")
# print(f"1 - Party, 2 - Vacation, Excused, Hall Pass, Haunted Mansion")
print(f"Party\nVacation\nExcused\nHall Pass\nHaunted Mansion")


def main():
    choice_count = 0
    while choice_count == 0:
        madlib_choice = input(f"which Madlib would you like to do? > ")
        # the following print statements have been used to test that my while/if stuff is working correctly.  Ultimately i'll remove them and put in more appropriate code.
        if madlib_choice.lower() == "party":
            madlibCongrats(madlib_choice)
            madlibParty()
            break
        elif madlib_choice.lower() == "vacation":
            madlibCongrats(madlib_choice)
            madlibVacation()
            break
        elif madlib_choice.lower() == "excused":
            madlibCongrats(madlib_choice)
            madlibExcused()
            break
        elif madlib_choice.lower() == "hall pass":
            madlibCongrats(madlib_choice)
            madlibHallPass()
            break
        elif madlib_choice.lower() == "haunted mansion":
            madlibCongrats(madlib_choice)
            madlibHauntedMansion()
            break
        else:
            print(f"Your choice of: {madlib_choice} doesn't match one of the options or is spelled incorrectly, please select again.")


def madlibFormatting():
    print("==========================================")

def madlibCongrats(choice):
    print("+=+==+===+====+=====+=====+====+===+==+=+")
    #print("\n\n")
    print(f"Congratulations {user_name} you've chosen the {choice.title()} MadLib!")
    print("You will be asked for some words and phrases to insert into your madlib.")
    #print("\n\n")
    print("+=+==+===+====+=====+=====+====+===+==+=+")

def madlibParty():
    #this madlib was taken from their website
    theme = input(f"please choose a theme for your party. > ")
    place = input(f"Please choose a location. > ")
    day_of_week = input(f"Choose a day of the week. > ")
    chosen_time = input(f"Please choose a time. > ")
    verb = input(f"please choose a verb. > ")
    animal = input(f"please choose an animal. > ")
    body_part = input(f"please select a body part. > ")
    contact_information = input(f"Finally, we need some contact information. > ")

    mad_lib_party_finished = f"""
    {user_name} is having a {theme} party!
    It's going to be at {place} on {day_of_week}.
    Please make sure to show up at {chosen_time}, or else you will be required to {verb} a {animal} with your {body_part}.
    RSVP at {contact_information}.
    This MadLib was created by {user_name} on {time_now_formatted}.
    """
    madlibFormatting()
    print(mad_lib_party_finished)
    madlibFormatting()


def madlibVacation():
    #this madlib was taken from their website
    vac_adjective01 = input("Adjective > ")
    vac_adjective02 = input("Adjective > ")
    vac_noun01 = input('Noun > ')
    vac_noun02 = input('Noun > ')
    vac_noun03 = input('Plural noun > ')
    vac_game01 = input('Game > ')
    vac_noun04 = input('Plural noun > ')
    vac_verbing01 = input('Verb ending in \'ing\' > ')
    vac_verbing02 = input('Verb ending in \'ing\' > ')
    vac_noun05 = input('Plural noun > ')
    vac_game02 = input('Game > ')
    vac_verbing03 = input('Verb ending in \'ing\' > ')
    vac_noun06 = input('Noun > ')
    vac_plant01 = input('Plant > ')
    vac_bodypart01 = input('Body part > ')
    vac_place = input('A place > ')
    vac_verbing04 = input('Verb ending in \'ing\' > ')
    vac_adjective03 = input("Adjective > ")
    vac_number = input('A number > ')
    vac_noun07 = input('Plural noun > ')

    mad_lib_vacation_finished = f"""
    A vacation is when you take a trip to some {vac_adjective01} place with your {vac_adjective02} family.  Usually you go to some place that is near a/an {vac_noun01} or up on a/an {vac_noun02}.  A good vacation place is one where you can ride {vac_noun03} or play {vac_game01} or go hunting for {vac_noun04}.  I like to spend my time {vac_verbing01} or {vac_verbing02}.  When parents go on a vacation, they spend their time eating three {vac_noun05} a day, and fathers play {vac_game02}, and mothers sit around {vac_verbing03}.  Last summer, my little brother fell in a/an {vac_noun06} and got poison {vac_plant01} all over his {vac_bodypart01}.  My family is going to go to (the) {vac_place}, and I will practice {vac_verbing04}.  Parents need vacations more than kids because parents are always very {vac_adjective03} and because they have to work {str(vac_number)} hours every day all year making enough {vac_noun07} to pay for the vacation.
    """

    madlibFormatting()
    print(mad_lib_vacation_finished)
    madlibFormatting()


def madlibExcused():
    #this madlib was taken from their website
    excuse_adjective = input('Please select an adjective > ')
    excuse_noun = input('Please select a noun > ')
    excuse_name = input('Please write the name of someone famous > ')

    mad_lib_excused_finished = f"""
    
    Date: {time_now_formatted}
    Please excuse {user_name}, who is far too {excuse_adjective} to attend {excuse_noun} class.
    Signed:
    {excuse_name.title()}

    """
    madlibFormatting()
    print(mad_lib_excused_finished)
    madlibFormatting()


def madlibHallPass():
    #this madlib was taken from their website
    hallpass_noun = input("Select a noun > ")
    hallpass_pronoun = input("What is your preferred pronoun? > ")
    hallpass_event = input("What is an event you'd like to attend? > ")
    hallpass_famous = input("Name a famous person > ")

    mad_lib_hallpass_finished = f"""
    
    Date: {time_now_formatted}
    {user_name} is too cool for {hallpass_noun.lower()} class.  Instead {hallpass_pronoun.lower()} will be attending {hallpass_event}.
    Signed:
    {hallpass_famous.title()}
    
    """
    madlibFormatting()
    print(mad_lib_hallpass_finished)
    madlibFormatting()


def madlibHauntedMansion():
    # This madlib was created from scratch
    man_adjective01 = input('Adjective > ')
    man_family_import = input('Family Name > ')
    man_verb01 = input('Past tense verb > ')
    man_verb02 = input('Past tense verb > ')
    man_verb03 = input('Past tense verb > ')
    man_adjective02 = input('Adjective > ')
    man_noun01 = input('Plural noun > ')
    man_name = input('Name of someone you don\'t like > ')
    man_noun02 = input('Plural noun > ')
    man_emotion = input('Emotion > ')
    man_number01 = str(input('Number > '))
    man_number02 = str(input('Number > '))
    man_verb04 = input('Verb ending in \'ing\' > ')
    man_verb05 = input('Verb ending in \'ing\' > ')
    man_famous = input('Famous person > ')
    man_verb06 = input('Verb > ')
    man_family = man_family_import.title()

    mad_lib_mansion_finished = f"""
    \tOnce there was a haunted Mansion in {man_adjective01} woods.  It was once owned by the {man_family} family.  
    For years there have been rumors that the {man_family} family {man_verb01}, {man_verb02}, and {man_verb03}; it sounds {man_adjective02}.  
    After the last {man_family} died the house has been haunted by {man_noun01}.  
    One day {man_name.title()} decided to investigate the mansion and was killed by a {man_noun02}.  
    Everyone in town was {man_emotion} about it.  Since then, there have been {man_number01} other people who have died in various ways from {man_verb04} to {man_verb05}.  
    In {man_number02} days, {man_famous.title()} will go into the Mansion to {man_verb06} the haunted {man_noun01} out.  
    """

    madlibFormatting()
    print(mad_lib_mansion_finished)
    madlibFormatting()










if __name__ == '__main__':
    main()
