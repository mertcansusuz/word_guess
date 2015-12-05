import random

def select_random_word():  # Function 1
    new_random_number = randint(0, len(words) - 1)
    return words[new_random_number]


def make_list():  # Function 2
    word = select_random_word()
    initialized_word = []
    word_list = list(word)
    for i in range(0, len(word_list)):
        if word_list[i] != " ":
            initialized_word.append("-")
        else:
            initialized_word.append(" ")
    return initialized_word, word


def guess_letter(char, word_dashes, word):  # Function 3
    list_word = list(word)
    if char in word:
        for i in range(0, len(list_word)):
            if char == list_word[i]:
                list_word[i] = char
                word_dashes[i] = char
        return True
    else:
        return False


name = raw_input("Please enter your name: ")
remaining_guess = 6
words = ["stack", "queue", "tree", "linked list", "software", "hardware", "operating systems", "algorithm", "computer",
         "network"]

wrong_letters = []

while True:
    new_word_dashed, new_word = make_list()
    while remaining_guess > 0:
        print "Remaining guess: %d" % remaining_guess
        print new_word_dashed
        #print_tree(remaining_guess)
        character = raw_input("Enter a letter:\n")
        if character in wrong_letters:
            print "Your entered a letter which you entered before."
            remaining_guess += 1
            pass
        if character == new_word:
            print "You won!"
            print "Your word is: %s" % new_word.upper()
            break
        else:
            if not guess_letter(character, new_word_dashed, new_word):
                remaining_guess -= 1
                wrong_letters.append(character)
            else:
                if "-" not in new_word_dashed:
                    print "You won!"
                    print "Your word is: %s" % new_word.upper()
                    break
                else:
                    pass
        if remaining_guess == 0:
            print "Your word is: %s" % new_word.upper()
            print name + " You have lost\n"
    any_input = raw_input("Do you want to play again?\nPress any key to play again.\nTo exit press 'no'\n")
    if any_input == "no":
        exit(0)
    wrong_letters = []
    remaining_guess = 6
