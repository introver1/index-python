customer_age=int(input("Enter your age: "))
day="wednesday"
price=12 if customer_age>=18 else 8
if day=="wednesday":
    price-=2
print("price for 1 ticket is $ ",price)


