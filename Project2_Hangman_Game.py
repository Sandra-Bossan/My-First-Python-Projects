# HANGMAN
import random

words = ['beethoven', 'hawaii', 'cappucino', 'chihuahua', 'obama', 'cherry']

chosen_word = random.choice(words)
word_display = ['_' for _ in chosen_word]
attempts = 5

print ("Ready to play Hangman? Let's go!")

while attempts > 0 and '_' in word_display:
    print('\n' + ''.join(word_display))
    guess = input('Guess a letter: ').lower()
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess
    else:
        print ('That letter does not occur in the word. You can do this!')
        attempts -=1

if '_' not in word_display:
    print('Well done! You guessed the word.')
    print(' '.join(word_display))
    print('Phew, you survived. Hooray!')
else:
    print('You have run out of attempts. The word is ' + chosen_word)
    print('Death! You lost.')