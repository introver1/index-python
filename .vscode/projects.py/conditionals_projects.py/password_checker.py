password=input("enter your password: ")
if len(password)>10:
    print("strong password")
elif len(password)>6 and len(password)<=10:
    print("medium password")
else:
    print('weak password')