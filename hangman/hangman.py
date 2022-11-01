import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


get_valid_word(words)


def hangman():
    print('<-----------------------------WELCOME TO HANGMAN-------------------------------->')
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed
    lives = 6
    while len(word_letters) > 0 and lives != 0:  # while the length of word letters is greater than 0
        # ' '.join(['a', 'b', 'cd']) ---> 'a b cd'
        print(f'and you have {lives} lives left,', " and you have used these letters: ", ' '.join(used_letters))

        # what current word  is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]   # to print out '-' if letter isn't
        # in used letters and is yet to be guessed
        print('current word: ', ' '.join(word_list))

        user_letter = input('guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives -= 1
                print(f"the letter {user_letter} is not in the word")
            if lives == 6:
                print("\n+-------------+")
                print("|             |")
                print("|             O")
                print("|              ")
                print("|              ")
                print("|              ")
                print("|              ")
                print("==             ")
            elif lives == 5:
                print("\n+-------------+")
                print("|             |")
                print("|             O")
                print("|             | ")
                print("|              ")
                print("|              ")
                print("|              ")
                print("==             ")
            elif lives == 4:
                print("\n+-------------+")
                print("|             |")
                print("|             O")
                print("|            /| ")
                print("|              ")
                print("|              ")
                print("|              ")
                print("==             ")
            elif lives == 3:
                print("\n+-------------+")
                print("|             |")
                print("|             O")
                print("|            /|\\ ")
                print("|              ")
                print("|              ")
                print("|              ")
                print("==             ")
            elif lives == 2:
                print("\n+-------------+")
                print("|             |")
                print("|             O")
                print("|            /|\\ ")
                print("|             | ")
                print("|              ")
                print("|              ")
                print("==             ")
            elif lives == 1:
                print("\n+-------------+")
                print("|             |")
                print("|             O")
                print("|            /|\\ ")
                print("|             | ")
                print("|            / ")
                print("|              ")
                print("==             ")
            elif lives == 0:
                print("\n+-------------+")
                print("|             |")
                print("|             O")
                print("|            /|\\ ")
                print("|             | ")
                print("|            / \\")
                print("|              ")
                print("==             ")
        elif user_letter in used_letters:
            print("you literally just guessed this word")

        else:
            print('invalid character')
    if lives == 0:
        print("\n you failed,sorry,the word was ", word)
    else:
        print("yay,you guessed the word ", word, ' correctly')


hangman()
