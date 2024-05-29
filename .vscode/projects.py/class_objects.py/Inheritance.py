# Creating a Parent Class
# A parent class is a class whose properties are inherited by the child class. 
# Let’s create a parent class called Person which has a Display method to display the person’s information.


# A Python program to demonstrate inheritance
class Person(object):
   
  # Constructor
  def __init__(self, name, id):
    self.name = name
    self.id = id
 
  # To check if this person is an employee
  def Display(self):
    print(self.name, self.id)
 
 
# Driver code
emp = Person("Introvert", 102) # An Object of Person
emp.Display()

# Creating a Child Class
# A child class is a class that drives the properties from its parent class. 
# Here Emp is another class that is going to inherit the properties of the Person class(base class).


class Emp(Person):

    def Print(self):
	    print("Emp class called")
	
Emp_details = Emp("Mayank", 103)

# calling parent class function
Emp_details.Display()

# Calling child class function
Emp_details.Print()


class Student:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def details(self):
        print(f"The name of student of id {self.id} is {self.name}.")
class Programmer(Student):
    def showlanguage(self):
        print('The default language of this student is Python.')

e=Programmer("Raja Kumar",420)
e.details() 
e.showlanguage()       
e2=Programmer("Rajat kumar",421)
e2.details()
e2.showlanguage()
