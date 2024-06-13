# a= True
# print(a:=False)



# num=[1,2,3,4,5]
# while(n:=len(num))>0:
#     print(num.pop())


# walrus operator :=
# new to python 3.8
# assignment expression aka walrus operator
# assigns value to variables as part of a larger expression

# happy =True
# print(happy)

# print(happy:=False)


foods = list()
while True:
    food = input("What food do you like?: ")

    # if food =="quit":
    #     break

    foods.append(food)

    # print(foods)
    # if len(foods) ==5:
        # print(f"The five foods you like : {foods}")
        # break
    
  

#  Doing same programme using walrus

# foods=list()
# while (food:=input("What do you like in fruits? ")) != "quit":
#     foods.append(food)  