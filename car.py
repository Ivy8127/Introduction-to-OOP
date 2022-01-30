



class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model
    def description(self):
        return f"This is a {self.color} {self.model} car"    

tesla = Car("red","ABX") #prints , this is a red ABX car
print(tesla.description()) 