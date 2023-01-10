import random
import random

# function below prompts the user for a custom word list. If none is provided, the default word list is used. TODO: GET BETTER DEFAULT LIST
def get_word_list():
    
    
    custom_list = input("Would you like to import a custom list of possible words? Type y for yes or n for no: ")
    while True:
        if custom_list == 'n' OR custom_list == '':  
            print("Okay, the default word list will be used") 
            return ['canal', 'brush', 'float', 'flame', 'favor', 'marry', 'lever',
             'large', 'crack', 'crime', 'alien', 'alloy', 'fairy', 'hotel', 'laser', 'knock']
         
    
        elif custom_list == 'y':
            new_list = input("Please input your custom word list with no commas: ")
            new_list = new_list.split(' ')
            return new_list
        
        else:
            custom_list = ("Please type y for yes or n for no: ")


# funcion below chooses a random word from the provided list of words.
def choose_word(wlist):
    print("Choosing word, please wait...")
    n = random.randint(0, (len(wlist) - 1))
    print("Done!")
    return wlist[n]

# function below is the main loop of the game. this is the only funtion to call other functions.
def play_game():
while True:
    word_list = get_word_list()
    word = choose_word(word_list)
    attempts = int(input("Please input how many attemts you would like. Leave blank for the default of 5 attempts."))



# main program body
print("Welcome to Purdle, a text-based customizable version of the popular game Wordle in Python.")
play_game()
