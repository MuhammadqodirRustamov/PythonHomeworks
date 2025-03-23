import random


accepted_yes_list = ['Y', 'YES', 'y', 'yes', 'ok']

while True:
    num = random.randint(1, 100)
    print(num)
    correct = False
    for i in range(10):
        guess = int(input(f"Enter your guess({10 - i} attemts left): ")) if i == 0 else int(input(f"Try again({10 - i} attemts left): "))
        if guess == num:
            correct = True
            print("-------------------------------")
            print("    You guessed it right!")
            print("-------------------------------")
            break
        elif guess > num:
            print("Too high!   ")
        else:
            print("Too low!   ")
    if correct:
        break
    else:
        print("-------------------------------")
        print("          GAME OVER")
        print("-------------------------------")
        if input("You lost the game. Want to play again? ") in accepted_yes_list:
            print("\n")
            print("-------------------------------")
            print("           NEW GAME")
            print("-------------------------------")
        else:
            break