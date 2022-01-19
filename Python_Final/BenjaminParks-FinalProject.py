# INF360 - Programming in Python
# Benjamin Parks
# Final Project

""" This project will be a tool used when playing the Mutants and Masterminds RPG. This game uses a table to tell players what
 players can and can't do with their charachters. It can take some time to lookup the players rank and the corresponding trait
 this program will simplify the process by asking users to input their charachters rank for each trait and will then print
 the limits of what their charachter can do. The first version will focus on their strength output and will tell the player
 how much the charachter can lift. Later versions can communicate how fast a charachter is. """



import logging
logging.basicConfig(filename='finalProgramlog.txt',
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')




# import table from finalTable.py file. File is put in seperate file to clean up program.
# use logging.debug statments to log a sucessful import or a failed one.
try:
    import finalObjects
    logging.debug('The objects were successfully imported!')
except:
    logging.critical("The objects were not imported")


# Create a function that will ensure the variable captured is an integer.
# The function will also ensure the integer is between 0 and 30
def inputStrNumber(message):
    while True:
        try:
            userInput = int(input(message))
            if userInput < 0 or userInput > 30:
                raise ValueError
                raise TypeError
        except ValueError:
            print('This value must be an integer between 0 and 30')
        except TypeError:
            print('This input must be an integer between 0 and 30')
            continue
        else:
            return userInput
            break

# create strLevel variable 
strLevel = inputStrNumber('What is your character\'s strength level? ')

''' Uses strLevel variable within a function to find the object,
attribute that will tell player how much a character can lift'''

def canLift():
    if strLevel == 0:
        print('Your character can lift {}!' .format(finalObjects.RankZero.mass))
    elif strLevel == 1:
        print('Your character can lift {}!' .format(finalObjects.RankOne.mass))
    elif strLevel == 2:
        print('Your character can lift {}!' .format(finalObjects.RankTwo.mass))
    elif strLevel == 3:
        print('Your character can lift {}!' .format(finalObjects.RankThree.mass))
    elif strLevel == 4:
        print('Your character can lift {}!' .format(finalObjects.RankFour.mass))
    elif strLevel == 5:
        print('Your character can lift {}!' .format(finalObjects.RankFive.mass))
    elif strLevel == 6:
        print('Your character can lift {}!' .format(finalObjects.RankSix.mass))
    elif strLevel == 7:
        print('Your character can lift {}!' .format(finalObjects.RankSeven.mass))
    elif strLevel == 8:
        print('Your character can lift {}!' .format(finalObjects.RankEight.mass))
    elif strLevel == 9:
        print('Your character can lift {}!' .format(finalObjects.RankNine.mass))
    elif strLevel == 10:
        print('Your character can lift {}!' .format(finalObjects.RankTen.mass))
    elif strLevel == 11:
        print('Your character can lift {}!' .format(finalObjects.RankEleven.mass))
    elif strLevel == 12:
        print('Your character can lift {}!' .format(finalObjects.RankTwelve.mass))
    elif strLevel == 13:
        print('Your character can lift {}!' .format(finalObjects.RankThirteen.mass))
    elif strLevel == 14:
        print('Your character can lift {}!' .format(finalObjects.RankFourteen.mass))
    elif strLevel == 15:
        print('Your character can lift {}!' .format(finalObjects.RankFifteen.mass))
    elif strLevel == 16:
        print('Your character can lift {}!' .format(finalObjects.RankSixteen.mass))
    elif strLevel == 17:
        print('Your character can lift {}!' .format(finalObjects.RankSeventeen.mass))
    elif strLevel == 18:
        print('Your character can lift {}!' .format(finalObjects.RankEighteen.mass))
    elif strLevel == 19:
        print('Your character can lift {}!' .format(finalObjects.RankNineteen.mass))
    elif strLevel == 20:
        print('Your character can lift {}!' .format(finalObjects.RankTwenty.mass))
    elif strLevel == 21:
        print('Your character can lift {}!' .format(finalObjects.RankTwentyone.mass))
    elif strLevel == 22:
        print('Your character can lift {}!' .format(finalObjects.RankTwentytwo.mass))
    elif strLevel == 23:
        print('Your character can lift {}!' .format(finalObjects.RankTwentythree.mass))
    elif strLevel == 24:
        print('Your character can lift {}!' .format(finalObjects.RankTwentyfour.mass))
    elif strLevel == 25:
        print('Your character can lift {}!' .format(finalObjects.RankTwentyfive.mass))
    elif strLevel == 26:
        print('Your character can lift {}!' .format(finalObjects.RankTwentysix.mass))
    elif strLevel == 27:
        print('Your character can lift {}!' .format(finalObjects.RankTwentyseven.mass))
    elif strLevel == 28:
        print('Your character can lift {}!' .format(finalObjects.RankTwentyeight.mass))
    elif strLevel == 29:
        print('Your character can lift {}!' .format(finalObjects.RankTwentynine.mass))
    elif strLevel == 30:
        print('Your character can lift {}!' .format(finalObjects.RankThirty.mass))


# Declare the function to get output.
canLift()
 

