import random

NUM_DIGITS = 2  # number of digits
WORD = 1  # number in Word
MAX_GUESSES = 10  # Chances of guesses

def getSecret():
    secret_num = ''.join(random.choice('0123456789abcde') for _ in range(NUM_DIGITS))
    secret_word = ''.join(random.choice('abcde') for _ in range(WORD))
    return secret_num, secret_word

def getClue(guess, secret_num, secret_word):
    clue = ''
    for i in range(NUM_DIGITS):
        if guess[i] == secret_num[i]:
            clue += 'Fermi '
        elif guess[i] in secret_num:
            clue += 'Pico '
    for i in range(WORD):
        if guess[NUM_DIGITS + i] == secret_word[i]:
            clue += 'Fermi '
        elif guess[NUM_DIGITS + i] in secret_word:
            clue += 'Pico '
    if not clue:
        clue = 'Bagels'
    return clue

def main():
    print('''
Bagel for both number and letter

I am thinking of a {}-digit number with no repeated digits or a letter word but can be repeated.
When I say: I means:
 Pico        One digits or letter is correct but the wrong positon
 Fermi       One digits or letter is correct and the right direction
 Bagels      No digits or letter is right

For example, if the secret number is 349 and  letter is 'FROM' and your guess was 345 and four, the clues would be Fermi pico'''.format(NUM_DIGITS, WORD))
    
    while True:
        secret_num, secret_word = getSecret()
        print('I have thought of a number and letter for you')
        print('You have {} guesses to get it'.format(MAX_GUESSES))

        numGuess = 1
        while numGuess <= MAX_GUESSES:
            guess = input('Enter your {}-digit number and {}-letter word: '.format(NUM_DIGITS, WORD))
            if len(guess) != NUM_DIGITS + WORD:
                print('Invalid input. Please enter a {}-digit number and {}-letter word.'.format(NUM_DIGITS, WORD))
                continue
            clue = getClue(guess, secret_num, secret_word)
            print(clue)
            if guess == secret_num + secret_word:
                print('Congratulations! You won!')
                break
            numGuess += 1
        else:
            print('Sorry, you ran out of guesses. The secret number was {} and the secret word was {}.'.format(secret_num, secret_word))
        if numGuess > MAX_GUESSES:
            print('Do you want to play again')
            if not input('> ').lower().startswith('y'):
                break
    print('Thanks for playing')

if __name__ == '__main__':
    main()