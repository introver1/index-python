import random
num = 5
Random_number = random.randint(0, num)
Guessing_number = Random_number 
while True:
    user_pick = int(input("Enter your choice: "))
    if user_pick==Guessing_number:
        print("You guess the right number.")
        break
    elif user_pick>Guessing_number :
        print("You have guess bigger number. Pls, Guess smaller number")
    else:
        print("You have guess smaller number.Pls, Guess smaller number.")



# Guess the number using function
import random
# def guess(num):
#     random_number=random.randint(1,num)
#     while True:
#         guessing_number=int(input(f"Guess a number between 1 to {num}."))
#         if random_number==guessing_number:
#             print("Congrats!! you have guess correct number.")
#             break
#         elif random_number>guessing_number:
#             print("Too low. Please, Guess higher number.")
#         else:
#             print("Too high. Please, Guess lower number.")
# Computer Guessing
def computer_guess(num):
    low=1
    high=num
    feedback=""
    while feedback!="c":
        if low!=high:
            guess=random.randint(1,num)
        else:
            guess=low
        feedback = input(f"is {guess} is too high(h), too low(l), and correct(c)").lower()
        if feedback=="h":
            high=guess-1
        elif feedback=="l":
            low=guess+1    
    print("Yes!!! computer have guessed your number, {guess} correctly.")        
computer_guess(1000)
# guess(1000)          
