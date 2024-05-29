import random
user_wins=0
computer_wins=0
options=["snake","water","gun"]
user_choice=input("enter snake/water/gun: ").lower()
random_number=random.randint(0,2)
computer_choice=options[random_number]
print("computer picked", computer_choice +".")
if user_choice =="snake" and computer_choice=="water":
    print("You won! ")
    user_wins += 1
elif user_choice =="water" and computer_choice=="gun":
    print("You won! ")
    user_wins += 1
elif user_choice =="gun" and computer_choice=="snake":
    print("You won! ")
    user_wins += 1
else:
    print("Computer won!")
    computer_wins += 1
print("you won ", user_wins,  "times.")
print("computer won", computer_wins, "times.")
print("Thank you! for playing games.")