# Pluralsight games
import random

print("Let the games begin!")


def get_words():
    words = ['into', 'dust', 'by', 'yes', 'boss']
    word = random.choice(words)

    return word


def blanks(word):
    for i in word:
        print(i, " ", end="")
    print("")


def get_guess():
    print("Enter a letter")
    return input()


def process_letter(letter, word, blanked_word):
    if letter in word:
        position = word.index(letter)
        word[position] = letter
        return blanked_word


def main():
    chances = 0
    max_chance = 3
    playing = True

    Word = get_words()
    print(Word)
    blanked_word = list("_ " * len(Word))

    # print(blanked_word)

    while playing:
        blanks(blanked_word)
        word_list = list(Word)
        letter = get_guess()
        new_blanks = process_letter(letter, word_list, blanked_word)
        print (new_blanks)
        if not new_blanks:
            chances += 1
        if new_blanks == Word:
            print("You got it")
            playing = False
        if chances >= max_chance:
            playing = False
    if chances >= max_chance:
        print("loser")
    else:
        print("winner")


    # while playing:
    #     blanked_word = blanks(Word)
    #     letter = get_guess()
    #     print(Word)
    #     lst = list(Word)
    #     blk = process_letter(letter, lst, blanked_word)
    #     print (blk)
    #     chances += 1
    #     print(chances)
    #     if letter in full:
    #         print("one step at a time")

    #     if chances >= max_chance:
    #         playing = False
    #         print("You're out of luck")

    # if chances >= max_chance:
    #     print("loser")
    # else:
    #     print("winner")


main()
