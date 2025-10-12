class Car:
    def __init__(self,name,brand):
        self.name=name
        self.brand=brand
        
    def driving(self):
        print("the car is ",self.brand,"and by ",self.name)
        


car=Car("dirsan","toyota")
car.driving()