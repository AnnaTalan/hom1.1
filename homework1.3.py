class Automobile:
 
    def __init__(self, color, model, price):
        self.color = color
        self.model = model
        self.price = price
 
    def __str__(self):
        return self.model + ": " + self.color + ", " + self.price + " usd."
 
car1 = Automobile("White", "Bmw", "10 millions ")
car2 = Automobile("Blue", "Nissan", "4 millions ")
car3 = Automobile("Red", "Honda", "7 millions ")
print(car1)
print(car2)
print(car3)
