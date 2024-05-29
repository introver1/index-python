#  dir, __dict__ and help() functions
#  __dict__ is an attribute


x= [1,2,3]
print(dir(x))
print(x.__add__)
print(x.__sizeof__)


#  By using dict method we can print class in dictionaries
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

a = person("Introvert", 20) 
print(a.name, a.age)       
print(a.__dict__)



# using help method
#  It show every method used in class
print(help(person))