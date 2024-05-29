# Example

# Here, we are using the enumerate() function with both a list and a string. Creating enumerate objects for each and displaying their return types.
# It also shows how to change the starting index for enumeration when applied to a string,
#  resulting in index-element pairs for the list and string.


l1=["iron","gold","silver","bronze","copper"]
l2=["introvert"]
obj1=enumerate(l1)
obj2=enumerate(l2)

print("return type:",obj1)
print(list(obj1))
print(list(obj2))
print (list(enumerate(l2, 2)))




l3=["raja","rani","gopal","govinda","ajay"]
for ele in enumerate(l3):
    print(ele)

for count, ele in enumerate(l3, 100):
    print (count, ele)    

# getting desired output from tuple
for count, ele in enumerate(l3):
    print(count)
    print(ele)    