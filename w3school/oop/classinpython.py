# class Car:
#     def __init__(self,name,brand):
#         self.name=name
#         self.brand=brand
        
#     def driving(self):
#         print("the car is ",self.brand,"and by ",self.name)
        


# car=Car("dirsan","toyota")
# car.driving()


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def __str__(self):
        return f" Name: {self.name},Age: {self.age}"
    
    
person=Person("dirsan",21)

print(person)