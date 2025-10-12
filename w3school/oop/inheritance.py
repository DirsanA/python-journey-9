class Animal:
    def __init__(self,name):
        self.name=name
        
        
    def sound(self):
        return "Some Sound"

#  the dog class that inherit class of animal
class Dog(Animal):
    def sound(self):
        print("woo woo")
        
        
class Cat(Animal) :
    def sound(self):
        print("mowwwwwwwww")
        
        
dog=Dog("dog")


print("Name ",dog.name,"sound ",dog.sound())
