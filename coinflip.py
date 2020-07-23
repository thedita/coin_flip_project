import random
print 'Welcome to the Game of Chance!'
print 'Which game would you like to play?'

correct_guesses = 0
total_guesses = 0

def make_guess():
    print "Correct Guesses:", correct_guesses
    print "Total Guesses:", total_guesses
    guess = raw_input('Guess either Heads or Tails\n')
    return guess

def make_dice_guess():
    print "Correct Guesses:", correct_guesses
    print "Total Guesses:", total_guesses
    guess = raw_input('Guess a number from 1-6\n')
    return guess
    
def print_result(str):
    print 'You got %s!' % str
    
def quit_or_again():
    answer = raw_input('Type "Quit" to exit. Press space to play again.\n')
    if answer == 'quit' or answer == 'Quit':
        quit()
    else:
        which_game()
    
def flip_coin(guess):
    flip = random.choice([1, 2])
    if flip == 1:
        result = "Heads"
    else:
        result = "Tails"
    print_result(result)
    global total_guesses
    total_guesses += 1
    if result == guess:
        global correct_guesses
        correct_guesses += 1
        print 'You guessed correctly!'
    elif result != guess:
        print 'You guessed incorrectly!'
    quit_or_again()

def roll_dice(guess):
    roll = random.choice([1, 2, 3, 4, 5, 6])
    print 'You rolled a %d!' % roll
    global total_guesses
    total_guesses += 1
    if roll == guess:
        global correct_guesses
        correct_guesses += 1
        print 'You guessed correctly!'
    elif roll != guess:
        print 'You guessed incorrectly!'
    quit_or_again()

def which_game():
    game = int(raw_input('Enter 1 for Coin Flip and 2 for 6-sided dice\n'))
    if game == 1:
        coin_guess = make_guess()
        flip_coin(coin_guess)
    elif game == 2:
        dice_guess = make_dice_guess()
        roll_dice(dice_guess)
which_game()

