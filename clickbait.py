"""Clickbait Headline Generator, by Al Sweigart al@inventwithpython.com
A clickbait headline generator for your soulless content farm website.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: large, beginner, humor, word"""

from locale import ERA
import random
from re import L

# Set up the constants:
OBJECT_PRONOUNS = ['Her', 'Him', 'Them']
POSSESIVE_PRONOUNS = ['Her', 'His', 'Their']
PERSONAL_PRONOUNS = ['She', 'He', 'They']
# Original Static Lists
"""
STATES = ['California', 'Texas', 'Florida', 'New York', 'Pennsylvania',
          'Illinois', 'Ohio', 'Georgia', 'North Carolina', 'Michigan']
NOUNS = ['Athlete', 'Clown', 'Shovel', 'Paleo Diet', 'Doctor', 'Parent',
         'Cat', 'Dog', 'Chicken', 'Robot', 'Video Game', 'Avocado',
         'Plastic Straw','Serial Killer', 'Telephone Psychic']
PLACES = ['House', 'Attic', 'Bank Deposit Box', 'School', 'Basement',
          'Workplace', 'Donut Shop', 'Apocalypse Bunker']
WHEN = ['Soon', 'This Year', 'Later Today', 'RIGHT NOW', 'Next Week']
"""
# new and improved static lists
STATES = ['Alabama', 'Alaska', 'American Samoa', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Guam', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Minor Outlying Islands', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Northern Mariana Islands', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Puerto Rico', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'U.S. Virgin Islands', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
NOUNS = ['Athlete', 'Clown', 'Shovel', 'Paleo Diet', 'Doctor', 'Parent', 'Cat', 'Dog', 'Chicken', 'Robot', 'Video Game', 'Avocado', 'Plastic Straw','Serial Killer', 'Telephone Psychic', 'Chihuahua', 'President', 'iPhone', 'Potato', 'Facebook', 'Tick Tock', 'Instagram', 'Orange', 'Governor']
PLACES = ['House', 'Attic', 'Bank Deposit Box', 'School', 'Basement', 'Workplace', 'Donut Shop', 'Apocalypse Bunker', 'Dildo Shop', 'Landscaping Company']
WHEN = ['Soon', 'This Year', 'Later Today', 'RIGHT NOW', 'Next Week', 'Today', 'Tomorrow', '50 Years From Now', 'At Somepoint', 'Next Monday']
ERA_TIME = ['20s', '30s', '40s', '50s', '60s', '70s', '80s', '90s', 'Naughts']
FILTERS = ['B&W', 'Color', 'Minimalistic', 'Linework', 'Realistic', 'Abstract', 'Geometric', 'Americana', 'Japanese', ]
EMOTIONS = ['Frenzy', 'Trance', 'Meditation', 'Rage', 'Slump']



def main():
    print('Clickbait Headline Generator')
    print('By Al Sweigart al@inventwithpython.com')
    print()

    print('Our website needs to trick people into looking at ads!')
    while True:
        print('Enter the number of clickbait headlines to generate:')
        response = input('> ')
        if not response.isdecimal():
            print('Please enter a number.')
        else:
            numberOfHeadlines = int(response)
            break  # Exit the loop once a valid number is entered.

    for i in range(numberOfHeadlines):
        clickbaitType = random.randint(1, 18)

        if clickbaitType == 1:
            headline = generateAreMillenialsKillingHeadline()
        elif clickbaitType == 2:
            headline = generateWhatYouDontKnowHeadline()
        elif clickbaitType == 3:
            headline = generateBigCompaniesHateHerHeadline()
        elif clickbaitType == 4:
            headline = generateYouWontBelieveHeadline()
        elif clickbaitType == 5:
            headline = generateDontWantYouToKnowHeadline()
        elif clickbaitType == 6:
            headline = generateGiftIdeaHeadline()
        elif clickbaitType == 7:
            headline = generateReasonsWhyHeadline()
        elif clickbaitType == 8:
            headline = generateJobAutomatedHeadline()
        elif clickbaitType == 9:
            headline = generateWithoutDoingThis()
        elif clickbaitType == 10:
            headline = generateSurprisingTricks()
        elif clickbaitType == 11:
            headline = generateBiggestTrends()
        elif clickbaitType == 12:
            headline = generateLosingCustomers()
        elif clickbaitType == 13:
            headline = generateFlashback()
        elif clickbaitType == 14:
            headline = generateMcdonalds()
        elif clickbaitType == 15:
            headline = generateTattoos()
        elif clickbaitType == 16:
            headline = generateThisIsMost()
        elif clickbaitType == 17:
            headline = generateBusinessJeopardy()
        elif clickbaitType == 18:
            headline = generateLoveProgram()

        print(headline)
    print()

    website = random.choice(['wobsite', 'blag', 'Facebuuk', 'Googles',
                             'Facesbook', 'Tweedie', 'Pastagram'])
    when = random.choice(WHEN).lower()
    print('Post these to our', website, when, 'or you\'re fired!')


# Each of these functions returns a different type of headline:
def generateAreMillenialsKillingHeadline():
    noun = random.choice(NOUNS)
    return 'Are Millenials Killing the {} Industry?'.format(noun)


def generateWhatYouDontKnowHeadline():
    noun = random.choice(NOUNS)
    pluralNoun = random.choice(NOUNS) + 's'
    when = random.choice(WHEN)
    return 'Without This {}, {} Could Kill You {}'.format(noun, pluralNoun, when)


def generateBigCompaniesHateHerHeadline():
    pronoun = random.choice(OBJECT_PRONOUNS)
    state = random.choice(STATES)
    noun1 = random.choice(NOUNS)
    noun2 = random.choice(NOUNS)
    return 'Big Companies Hate {}! See How This {} {} Invented a Cheaper {}'.format(pronoun, state, noun1, noun2)


def generateYouWontBelieveHeadline():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)
    pronoun = random.choice(POSSESIVE_PRONOUNS)
    place = random.choice(PLACES)
    return 'You Won\'t Believe What This {} {} Found in {} {}'.format(state, noun, pronoun, place)


def generateDontWantYouToKnowHeadline():
    pluralNoun1 = random.choice(NOUNS) + 's'
    pluralNoun2 = random.choice(NOUNS) + 's'
    return 'What {} Don\'t Want You To Know About {}'.format(pluralNoun1, pluralNoun2)


def generateGiftIdeaHeadline():
    number = random.randint(7, 15)
    noun = random.choice(NOUNS)
    state = random.choice(STATES)
    return '{} Gift Ideas to Give Your {} From {}'.format(number, noun, state)


def generateReasonsWhyHeadline():
    number1 = random.randint(3, 19)
    pluralNoun = random.choice(NOUNS) + 's'
    # number2 should be no larger than number1:
    number2 = random.randint(1, number1)
    return '{} Reasons Why {} Are More Interesting Than You Think (Number {} Will Surprise You!)'.format(number1, pluralNoun, number2)


def generateJobAutomatedHeadline():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)

    i = random.randint(0, 2)
    pronoun1 = POSSESIVE_PRONOUNS[i]
    pronoun2 = PERSONAL_PRONOUNS[i]
    if pronoun1 == 'Their':
        return 'This {} {} Didn\'t Think Robots Would Take {} Job. {} Were Wrong.'.format(state, noun, pronoun1, pronoun2)
    else:
        return 'This {} {} Didn\'t Think Robots Would Take {} Job. {} Was Wrong.'.format(state, noun, pronoun1, pronoun2)


def generateWithoutDoingThis():
    noun = random.choice(NOUNS)
    return f'You’ll Never Get More {noun}s Without Doing This'


def generateSurprisingTricks():
    number = random.randint(5, 15)
    noun = random.choice(NOUNS)
    return f'{number} Surprising {noun} Tricks You Don\'t Know!'


def generateBiggestTrends():
    number1 = random.randint(5, 15)
    number2 = random.randint(5, 15)
    number3 = random.randint(1800, 2023)
    noun = random.choice(NOUNS)
    return f'The {number1} BIGGEST {noun} Trends of {number3} (You Won\'t Believe #{number2}!)'


def generateLoveProgram():
    number1 = random.randint(5, 15)
    noun = random.choice(NOUNS)
    return f"{number1} Reasons Why {noun}s Love This Workout Program"


def generateBusinessJeopardy():
    number1 = random.randint(5, 15)
    noun = random.choice(NOUNS)
    return f'The Top {number1} Ways You\'re Putting Your {noun} In Jeopardy'


def generateLosingCustomers():
    noun = random.choice(NOUNS)
    return f'Why You\'re Losing {noun}s How You Can Fix It.'


def generateThisIsMost():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)
    return f'This Is The Most {state} Way To Remember The {noun}\'s Guidelines On Coronavirus Social Distancing'


def theLastEver():
    # “The Last Flat Iron You Will Ever Need”
    pass


def styleTips():
    # “46 Life-Changing Style Tips Every Woman Should Know”
    pass


def generateTattoos():
    number1 = random.randint(5, 25)
    filter = random.choice(FILTERS)
    noun = random.choice(NOUNS)
    emotion = random.choice(EMOTIONS)
    return f'{number1} {filter} {noun} Tattoos That Will Have You In A {emotion}'


def generateMcdonalds():
    noun1 = random.choice(NOUNS)
    noun2 = random.choice(NOUNS)
    return f'We Need To Talk About {noun1}\'s {noun2} Bites'


def generateFlashback():
    noun = random.choice(NOUNS)
    era = random.choice(ERA_TIME)
    return f'{noun} Terms That Will Give You Intense {era} Flashbacks'







# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()


print(generateLosingCustomers())
