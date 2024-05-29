# Using normal function to achieve getters and setters behaviour

# To achieve getters & setters property, if we define normal get() and set() methods it will not reflect any special implementation. 
# For Example



# Python program showing a use 
# of get() and set() method in 
# normal function 





# class student:
#     def __init__(self,name=""):
#         self._name=name

# def get_name(self):
#     return self._name
# def set_name(self,x):
#     self._name=x
# obj2 = student()
# obj2.set_name("introvert")
# print(obj2.get_age())
# print(obj2._name)    

    
# Using property() function to achieve getters and setters behaviour

# In Python property()is a built-in function that creates and returns a property object. A property object has three methods, getter(), setter(),
# and delete(). property() function in Python has four arguments property(fget, fset, fdel, doc), 
# fget is a function for retrieving an attribute value. fset is a function for setting an attribute value.
# fdel is a function for deleting an attribute value. doc creates a docstring for attribute. 
# A property object has three methods, getter(), setter(), and delete() to specify fget, fset and fdel individually. For Example


# Python program showing a 
# use of property() function 


class Geeks: 
     def __init__(self): 
          self._age = 0
       
     # function to get value of _age 
     def get_age(self): 
         print("getter method called") 
         return self._age 
       
     # function to set value of _age 
     def set_age(self, a): 
         print("setter method called") 
         self._age = a 
  
     # function to delete _age attribute 
     def del_age(self): 
         del self._age 
     
     age = property(get_age, set_age, del_age)  
  
introvert = Geeks() 
  
introvert.age = 20
  
print(introvert.age)


