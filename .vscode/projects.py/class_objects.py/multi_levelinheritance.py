class animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species

    def show_details(self):
        print(f"The name of animal is {self.name}, and species is {self.species}")

class cat(animal):
    def __init__(self,name,breed):
        animal.__init__(self,name,species="cat")

    def show_details(self):
        animal.show_details(self)
        print(f"breed: {self.breed}")


class chubbycat(cat):
    def __init__(self,name,color):
        cat.__init__(self,name,breed="chubbycat")
        self.color=color

    def show_details(self):
        cat.show_details(self)
        print(f"color: {self.color}")



o=chubbycat("Pussy","Pink")
o.show_details()                          
print(chubbycat.mro())        
    