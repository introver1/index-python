# reverse a string using loop
string=input("enter a string: ")
reversed_string=""
for char in string:
    reversed_string=char+reversed_string

print("reverse form of string is: ",reversed_string)    

# Find the first non-repeated character in a given string.
for char in string:
    print(char)
    if string.count(char)==1:
        print("repeated character is: ", char)    
           

        break
