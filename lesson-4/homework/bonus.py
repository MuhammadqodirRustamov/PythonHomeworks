import random

comp = 0
user = 0

while comp < 5 and user < 5:
    c = random.choice(["rock", "paper", "scissors"])
    u = (input("Your choice:")).lower()
    if u == "rock":
        if c == "rock":
            print("Rock vs Rock → Tie")
            user += 1
            comp += 1
        if c == "paper":
            print("Paper covers Rock → You lose")
            comp += 1
        if c == "scissors":
            print("Rock crushes Scissors → You win")
            user += 1
    if u == "paper":
        if c == "":
            print("Paper vs Paper → Tie")
            user += 1
            comp += 1
        if c == "rock":
            print("Paper covers Rock → You win")
            user += 1
        if c == "scissors":
            print("Scissors cuts Paper → You lose")
            comp += 1
    if u == "scissors":
        if c == "scissors":
            print("Scissors vs Scissors → Tie")
            user += 1
            comp += 1
        if c == "rock":
            print("Rock crushes Scissors → You lose")
            comp += 1
        if c == "scissors":
            print("Scissors cuts Paper → You win")
            user += 1
    print(f"You: {user}  Computer: {comp}")
print("-----------------------------")
if comp == user:
    print("        TIE")
elif comp > user:
    print("        YOU LOSE")
else:
    print("        YOU WIN")
print("-----------------------------")