class Bank_Account:
    # this is how we define constructor in class __init__()
    def __init__(self, balance):
        self.balance = balance
    def _getit(self):
        return self.balance
    
account_1 = Bank_Account(1000)
print(account_1._getit())    


class Animal:
    # self is always passed in the methods of class
    def whatItIsAnimal(self):
        print('this is Animal class')
# this is how we inherits class
class Dog(Animal):
    def whatItIsDog(self):
        print('this is Dog class')
myDog = Dog()
myDog.whatItIsAnimal()
myDog.whatItIsDog()

class Shape():
    def calculate_area(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    # new defination of circle area
    def calculate_area(self):
        return 3.14 * self.radius * self.radius
class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length
    # new defination of square area    
    def calculate_area(self):
        return self.side_length * self.side_length

circle = Circle(5)
square = Square(4)

print(f"Area of the circle: {circle.calculate_area()}")
print(f"Area of the square: {square.calculate_area()}")

