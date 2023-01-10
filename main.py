import random
# Wordle game in Python made but Kyle W. for AP College Board. It is text-based and has as much customizability
# as I can put in it(maybe in the future if it gets a ui I'll add skins n stuff).

# TODO finish the letter check and print which letters were guessed correctly, finish breaking all loops upon finish/exit,
# add excteption handling to every user input.

# function below prompts the user for a custom word list. If none is provided, the default word list is used. TODO: GET BETTER DEFAULT LIST
def get_word_list():
    
    
    custom_list = input("Would you like to import a custom list of possible words? Type y for yes or n for no: ")
    while True:
        if custom_list == 'n' or custom_list == '' or custom_list == 'no':  
            print("Okay, the default word list will be used") 
            return ['canal', 'brush', 'float', 'flame', 'favor', 'marry', 'lever', 'large', 'crack', 'crime', 'alien', 'alloy', 'fairy', 'hotel', 'laser', 'knock']

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
    while True:
        


        # set up the chosen word
        word_list = get_word_list()
        word = choose_word(word_list)
        sliced_word = []
        for letter in word:
            sliced_word.append(letter)

        # set up number of attempts
        while True: 
            try:
                attempts = int(input("Please input how many attemts you would like. The default is 5 attempts: "))
                break
            except ValueError:
                print("Not a number. Please try again")
        
        # ask for initial guess and slice into list
        guess = str(input("Game is set up. Please enter your guess now: "))
        sliced_guess = []
        for l in guess:
            sliced_guess.append(guess)

        # loop for the actual guessing part
        for i in range(attempts):
            output = ['-', '-', '-', '-', '-']
            misplaced = []
            print('word: '+str(sliced_word))
            # check the guess for correct letters
            for x in range(5):
                if guess[x] == word[x]:
                    output[x] = word[x]
                else:
                    output[x] = '-'

            #check the guess for correct letters in the wrong spot
            for y in range(5):
                exist_count = word.count(guess[y])
                if exist_count > 0 and not guess[y] == word[y]:
                    misplaced.append(guess[y])


            # print correct and misplaced characters
            print(output)
            print("Misplaced letters: " + str(misplaced))
            
            # break guess loop if guess is correct
            break_loop = False
            if sliced_word == output:
                reset = input("You have guessed right! Would you like to reset? yes or no: ")
                if reset == 'yes' or reset == 'y':
                    break
                elif reset == 'no' or reset == '' or reset == 'n':
                    return 0
            else:
                # ask for new guess
                guess = str(input("Guess: "))
        

# main program body
print("Welcome to Purdle, a text-based customizable version of the popular game Wordle in Python.")
play_game()
print("Thanks for playing!")