import random

# function below prompts the user for a custom word list. If none is provided, the default word list is used. TODO: GET BETTER DEFAULT LIST
def get_word_list():
    
    
    custom_list = input("Would you like to import a custom list of possible words? Type y for yes or n for no: ")
    while True:
        if custom_list == 'n' or custom_list == '' or custom_list == 'no':  
            print("Okay, the default word list will be used") 
            return ['canal', 'brush', 'float', 'flame', 'favor', 'marry', 'lever',
             'large', 'crack', 'crime', 'alien', 'alloy', 'fairy', 'hotel', 'laser', 'knock']

        elif custom_list == 'y' or custom_list == 'yes':
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
    stop = False

    while True:
        # stop loop if desired
        if stop == True:
            break


        # set up the chosen word
        word_list = get_word_list()
        word = choose_word(word_list)
        sliced_word = []
        for letter in word:
            sliced_word.append(letter)

        # set up nimber of attempts and ask for initial guess
        attempts = int(input("Please input how many attemts you would like. The default is 5 attempts."))
        guess = str(input("Game is set up. Please enter your guess now: "))
        sliced_guess = []
        for l in guess:
            sliced_guess.append(guess)

        # loop for the actual guessing part
        while True:
            correct = [0, 0, 0, 0, 0]
            for x in range(5):
                if guess[x] == word[x]:
                    correct[x] = 1
                else:
                    correct[x] = 0


            if correct == [1, 1, 1, 1, 1]:
                ("You have guessed right! Would you like to reset? yes or no: ")

# main program body
print("Welcome to Purdle, a text-based customizable version of the popular game Wordle in Python.")
play_game()
