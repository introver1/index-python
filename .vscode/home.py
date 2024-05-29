# lang=["java","javascript","c","c++","python"]
# print(lang)
# for i in range(len(lang)):
#     print("before lamguage",i,"is", lang[1])

# for i in "introvert":
#     print(i)
# l1=[1,4,6,7]
# l2=[]
# for i in l1:
#     l2.append(i+1)
#     print(i+1)
# print(l2)   

# dict1 = {'a':'aalu','b':'bhalu','c':'chutiya'}
# print(dict1)
# keys=[]
# values=[]
# for item in dict1.items():
#     keys.append(item[0])
#     values.append(item[1])
# print("keys= ",keys)
# print("values= ",values)    


# Nested for loop
# num=int(input("enter a number: \n"))
# i,j=0,0
# for i in range(0,num):
#     print()
#     for j in range(0,i+1):
#         print("+", end=" ")
#

# sum up the numbers till some point
# n=int(input("enter a number: "))
# starting_point=0
# counter=1
# while counter<=n:
#     starting_point=starting_point+counter
#     counter+=1
#     print(starting_point)

# factorial series



# To check whether the number is odd or even using function statements
# n=int(input("enter a number: "))
# def check_odd_even():
#     if n %2 ==0:
#         print("It is an even number.")
#     else:
#         print("Its an odd number.")
# check_odd_even()

# Recursion in python
def show(n):
    while n>0:
        print(n)
        n=n-1
show(5)        
# def show(n):
#     if(n==0):
#         return
#     print(n)
#     show(n-1)
# show(5)    


def factorial(n):
    fact=1
    while n>0:
        fact=fact*n
        n=n-1
        # print(fact)  
    print(fact)     
factorial(5)        
