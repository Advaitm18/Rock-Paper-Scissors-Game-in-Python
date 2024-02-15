import random

name = input("Enter the Username: ")
while True:
     
    options = ["Rock", "Paper", "Scissors"]
    user = input("\nChoose --->    Rock    Paper    Scissors    ---> ").title()
    bot = random.choice(options)

    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(f"{name}: {user}\n")
    print(f"User2: {bot}")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    if user==bot:
        print("It is a tie!" + "\U0001F611")
    elif user=="Rock" and bot=="Scissors":
        print("You win!" + "\U0001F603")
    elif user=="Paper" and bot=="Rock":
        print("You win!" + "\U0001F603")
    elif user=="Scissors" and bot=="Paper":
        print("You win!" + "\U0001F603")
    else:
        print("User2 wins!" + "\U0001F605")
    print("Do you want to play again? (Yes/No)")
    ans = input().title()
    if ans =='No':
        break
    else:
        print("_________________________________________________________")
        
