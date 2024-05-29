# To print ,ultiplication table for a given number up to 10 but skip the fifth iteration
n=int(input("enter a number: "))
for i in range(1,11):
    if i==5:
        print("skip the fifth iteration ")   
        continue
    print(n,"X",i,"=",i*n)
   