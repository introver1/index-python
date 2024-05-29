# class animal:
#     def __init__(self,name,species):
#         self.name=name
#         self.species=species

#     def make_sound(self):
#         print("sound made by the animal")




# class dog(animal):
#     def __init__(self,breed):
#         animal.__init__(self,name="dog",species="dog")
#         self.breed=breed


#     def make_sound(self):
#         print("bark") 


# d=dog("dog","doggerman")
# d.make_sound()


# a=animal("dog","dog")
# a.make_sound()


# Quick quiz: Implement a cat class by using the animal class and add some methods 
# specific to cat


class animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species

    def make_sound(self):
        print(f"sound of an animal name {self.name} species of {self.species}")


class cat(animal):
    def __init__(self,name,breed):
        animal.__init__(self,name,species="cat")
        self.breed=breed

    def make_sound(self):
        print("meow!!! meow!!!")


a=animal("pussy","cat")
a.make_sound()

c=cat("cat","pussy")
c.make_sound()

