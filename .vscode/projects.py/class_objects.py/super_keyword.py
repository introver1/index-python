class parentclass:
    def parent_method(self):
        print("This is a parent class.")


class childclass(parentclass):
    def child_method(self):
        print("This is a child class.")
        super().parent_method()
        #  Using super() method we can call parent_method() inside child_method.

child_object = childclass()
child_object.child_method()
# child_object.parent_method()        




class employee:
    def __init__(self, name,id):
        self.name = name
        self.id = id

class programmer(employee):
    def __init__(self, name, id,lang):
        super().__init__(name, id)
        self.name = name
        self.id = id
        self.lang = lang



raja = employee("raja", 5678)
introvert = programmer("introvert", 234, "Python") 
print(introvert.name)
print(introvert.id)
print(introvert.lang)
