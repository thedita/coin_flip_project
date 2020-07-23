import random
correct_guesses = 0
total_guesses = 0

print 'Welcome to the Coin Flip Game!'
def make_guess():
    guess = raw_input('Guess either Heads or Tails\n')
    return guess
guess1 = make_guess()

raw_input('Press enter to flip the coin')

def print_result(str):
    print 'You got %s!' % str
    
def quit_or_again():
    answer = raw_input('Type "Quit" to exit. Press space to play again.\n')
    if answer == 'quit' or answer == 'Quit':
        quit()
    else:
        guess = make_guess()
        flip_coin(guess)
    
def flip_coin(guess):
    flip = random.choice([1, 2])
    if flip == 1:
        result = "Heads"
    else:
        result = "Tails"
    print_result(result)
    if result == guess:
        print 'You guessed correctly!'
    elif result != guess:
        print 'You guessed incorrectly!'
    quit_or_again()

flip_coin(guess1)

