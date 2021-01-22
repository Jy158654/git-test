def play_nim(pile,max_stone):
    while pile > 0:
        num_stones1 = input("Enter a number\nPlayer 1: ")
        while not num_stones1.isdigit():
            num_stones1 = input("Please enter a number!\nPlayer 1: ")
        while not 1 <= int(num_stones1) <= max_stone:
            num_stones1 = input("Please enter a number between 1 and {} inclusive!\nPlayer 1: ".format(max_stone))
            while not num_stones1.isdigit():
                num_stones1 = input("Please enter a number!\nPlayer 1: ")
        pile -= int(num_stones1)
        if pile <= 0:
            print("\nPlayer 1 won!\nGame Over!")
            break
        num_stones2 = input("Enter a number\nPlayer 2: ")
        while not num_stones2.isdigit():
            num_stones2 = input("Please enter a number!\nPlayer 2: ")
        while not 1 <= int(num_stones2) <= max_stone:
            num_stones2 = input("Please enter a number between 1 and {} inclusive!\nPlayer 2: ".format(max_stone))
            while not num_stones2.isdigit():
                num_stones2 = input("Please enter a number!\nPlayer 2: ")
        pile -= int(num_stones2)
        if pile <= 0:
            print("\nPlayer 2 won!\nGame Over!")

play_nim(100,10)




