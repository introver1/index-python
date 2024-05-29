# sum of even numbers to n numbers
n=int(input("enter a number: "))
sum=0
for loop in range(0,n):
    if loop %2 == 0:
        sum=loop+sum
print("total sum of even numbers to n numbers: ",sum)