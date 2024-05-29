num=int(input("enter a number: "))
if num>=1 and num<=10:
    print("validate input")
else:
    print("please, enter validate number")

# To find whether a number is prime or not
n=int(input("enter a number: "))
for i in range(1,n):
    if n % i !=0:
        print(True, "Its a prime number.")
        
    else:
        print(False, "It is not prime number.") 
