import random

print("Let the games begin!")


def get_words():
    words = ['into', 'dust', 'by', 'yes', 'boss']
    word = random.choice(words)

    return word


def get_guess():
    print("Enter a letter")
    return input()


def process_letter(letter, word, blanked_word):
    if letter in word:
        position = word.index(letter)
        blanked_word[position] = letter
        return blanked_word
    else:
        return blanked_word


def main():
    chances = 0
    max_chance = 3
    playing = True

    Word = get_words()
    print(Word)
    blanked_word = list("_" * len(Word))

    # print(blanked_word)

    while playing:
        # print(blanked_word)
        word_list = list(Word)
        letter = get_guess()
        new_blanks = process_letter(letter, word_list, blanked_word)
        joined = ''.join(new_blanks)
        print (joined)
        if not new_blanks:
            chances += 1
        if joined == Word:
            print("You got it")
            playing = False
        if chances >= max_chance:
            playing = False
    if chances >= max_chance:
        print("loser!")
    else:
        print("winner!")


main()
