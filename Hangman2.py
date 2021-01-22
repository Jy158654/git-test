import random

with open("my_file.txt","r") as myfile:
    random_line = random.choice(myfile.readlines())
    random_word = (random.choice(random_line.split(" "))).upper()
    while not random_word.isalpha() or len(random_word) < 3 or len(random_word) > 6:
        random_word = random.choice(random_line.split(" ")).upper()

print(random_word)

def word_length(wrd):
    line = ""
    wrd_len = len(wrd)
    if wrd_len == 3:
        line += "- "*3 + " "*3
    elif wrd_len == 4:
        line += "- "*4 + " "*2
    elif wrd_len == 5:
        line += "- "*5 + " "*1
    elif wrd_len == 6:
        line += "- "*6
    return line.split(" ")

def split_word(word):
    return [char for char in word]

def play_hangman():
    global guess
    guess_list = [" ", " ", " ", " ", " ", " "]
    word_list = split_word(random_word)
    guess_word_list = []
    wrong_guess = []
    goal = 0

    #opening
    print("Welcome to hangman! Can you guess the correct word?\nYou have three chances!\n")
    word_len = word_length(random_word)
    print("{} {} {} {} {} {}".format(word_len[0], word_len[1], word_len[2], word_len[3], word_len[4], word_len[5]))
    print("____________")
    print("|          |")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")

    chances = 5
    while chances > 0:
        print("\nChance left: {}".format(chances))
        guess_word = input("Enter an alphabet: ").upper()
        if guess_word.isalpha() and len(guess_word) == 1:     #if input is valid
            if guess_word in guess_word_list:                                          #condition 1(guess correct)
                print("You have already guessed {} before.".format(guess_word))
                continue
            if guess_word in word_list and word_list.count(guess_word) == 1:           #condition 2(guess correct)
                index = word_list.index(guess_word)
                guess_list[index] = word_list[index]
                guess = " ".join(guess_list)
                print("\n" + guess)
                print("{} {} {} {} {} {}".format(word_len[0], word_len[1], word_len[2], word_len[3], word_len[4], word_len[5]))
                guess_word_list.append(guess_word)
                goal += 1
            elif guess_word in word_list and word_list.count(guess_word) >= 1:         #condition 3(guess correct)
                while word_list.count(guess_word) >= 1:
                    index = word_list.index(guess_word)
                    guess_list[index] = word_list[index]
                    word_list[index] = " "
                    goal += 1
                guess = " ".join(guess_list)
                print("\n" + guess)
                print("{} {} {} {} {} {}".format(word_len[0], word_len[1], word_len[2], word_len[3], word_len[4],word_len[5]))
                guess_word_list.append(guess_word)

            else:
                if guess_word not in wrong_guess:                               #condition 1(guess incorrect)
                    print("Oops, it's not in the word!")
                    wrong_guess.append(guess_word)
                    chances -= 1
                else:
                    print("You have guessed {} before".format(guess_word))      #condition 2(guess incorrect)
            if goal == len(random_word):
                print("Congratulations! You got the word!")
                break

        else:
            print("Invalid input")
        if chances == 0:
            print("\nGame Over! Rest in peace!")
        print("____________")
        print("|          |")
        print("|          " + ("O" if chances < 5 else ""))
        print("|         " + (" |" if chances == 3 else "")+("/|\\" if chances < 3 else ""))
        print("|         " + ("/" if chances < 2 else "") + (" \\" if chances < 1 else ""))
        print("|")
        print("|")


play_hangman()


#two things new
#1)joining guess_list to print alphabet on respective places
#2)"0" if chances < 3 else ""