from random import randint
board = []

for i in range(5):
    board.append(["O"]*5)

print()
print("Sink my ship! You have 4 chances!")


def print_board(board_list):
    for row in board_list:
        print("".join(row))


print_board(board)


def random_row(boards):
    return randint(0, len(board)-1)


def random_col(boards):
    return randint(0, len(board)-1)


generated_row = random_row(board)
generated_col = random_col(board)
print(generated_row)
print(generated_col)

for turn in range(1, 5):
    print("Turn: " + str(turn))
    guess_row = int(input("Guess a row: ")) - 1
    guess_col = int(input("Guess a column: ")) - 1
    if guess_row == generated_row and guess_col == generated_col:
        print("Congratulations, you sunk my ship!")
        break
    else:
        if guess_row not in range(0, len(board)) or guess_col not in range(0, len(board)):
            print("It's not even in the ocean!")
        elif board[guess_row][guess_col] == "X":
            print("You guessed this before already!")
        else:
            board[guess_row][guess_col] = "X"
            print("You missed the ship, try again!")
        print_board(board)
        print()
        if turn == 4:
            print("Game Over")


#one thing
#board[guess_row][guess_col]  --> sublist in list for row and column


