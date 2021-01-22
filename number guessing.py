import random

def check_guessed_number(num):
    while not num.isdigit():
        print("Invalid input...")
        num = input("Guess a number: ")
    else:
        return int(num)


def play_game():
    turn = 1
    score = 100
    print("Round: {}".format(turn))
    guessed_number = input("Guess a number: ")
    check_guessed_number(guessed_number)
    number_guessed = check_guessed_number(guessed_number)
    number_generated = random.randint(0, int(check_guessed_number(guessed_number)) + 20)
    turn += 1
    print(number_generated)
    while number_guessed != number_generated:
        score = score * 0.9
        if number_guessed - number_generated > 10:
            print("The number is too large!")
            print("")
            print("Round: {}".format(turn))
            turn += 1
            guessed_number = input("Guess a number: ")
            check_guessed_number(guessed_number)
            number_guessed = check_guessed_number(guessed_number)

        elif number_generated - number_guessed > 10:
            print("The number is too small!")
            print("")
            print("Round: {}".format(turn))
            turn += 1
            guessed_number = input("Guess a number: ")
            check_guessed_number(guessed_number)
            number_guessed = check_guessed_number(guessed_number)

        elif (number_guessed - number_generated) <= 10 or number_generated - number_guessed <= 10:
            print("You are almost there!")
            print("")
            print("Round: {}".format(turn))
            turn += 1
            guessed_number = input("Guess a number: ")
            check_guessed_number(guessed_number)
            number_guessed = check_guessed_number(guessed_number)
    else:
        print("")
        print("Congratulations! You won!")
        print("Score: {}".format(score))

play_game()