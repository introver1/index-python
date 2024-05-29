import random
# user_wins=0
# computer_wins=0
# options=["scissors","paper","rock"]
# user_input=input("choose rock,paper,scissors: ").lower()
# random_number=random.randint(0,2)
# computer_pick=options[random_number]
# print("computer pick",computer_pick + ".")
# if user_input=="scissors" and computer_pick=="paper":
#     print("you won")
#     user_wins += 1
# elif user_input=="rock" and computer_pick=="scissors":
#     print("you won")
#     user_wins += 1
# elif user_input=="paper" and computer_pick=="rock":
#     print("you won")
#     user_wins += 1
# else:
#     print("computer won.")
#     computer_wins += 1
# print("you won", user_wins, "times.")        
# print("computer won", computer_wins, "times")
# print("Thank you for playing games.")        


def play():
    options= ['s','p','r']
    user_guess=input("Enter 's' for scissors, 'p' for paper,'r' for rock. ").lower()

    random_number=random.randint(0,2)
    computer_options= options[random_number]
    print(f"Computer picks {computer_options}. ")
    while True:
        if user_guess=="s"and computer_options=="p" or user_guess=="p"and computer_options=="r" or user_guess=="r"and computer_options=="s":
            print("You have won the game.") 
            break
        elif computer_options==user_guess:
            print("Tie, Please, Try again.")
            break
    # elif user_guess=="p"and computer_options=="r":
    #     print("You have won the game.")
    # elif user_guess=="r"and computer_options=="s":
    #     print("You have won the game.")
    else:
        print("Computer have won.")
play()        