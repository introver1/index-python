# Differences between Instances and Class
class Employee:
    company_name = "Gooluluu"
    no_of_Employee = 0
    def __init__(self, name):
        self.name=name
        self.raise_amount = 0.2
        Employee.no_of_Employee +=1
    def showdetails(self):
        print(f"The name of the Employee is {self.name}. and The raise amount in {self.company_name} of sized {self.no_of_Employee} is {self.raise_amount}")

a1 = Employee("Introvert")
a1.raise_amount = 0.5
a1.company_name = "Nepal goolulu" 
a1.showdetails()
a2 = Employee("Raja")
a2.showdetails()
