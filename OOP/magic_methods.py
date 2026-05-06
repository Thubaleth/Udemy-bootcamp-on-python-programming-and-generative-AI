class Robot:
    """This class implements a robot"""
    population = 0 #class attribute(like a counter)
    def __init__(self,name,price):
        self.name = name
        self.price = price
        Robot.population +=1
    def __del__(self):
        print("Robot destroyed")
    
    def __str__(self):
        my_str = f'My name is {self.name} and my price is {self.price}'
        return my_str
    def __add__(self,other): #because we comparing two prices
        price = self.price + other.price
        return price

r1 = Robot("Marvin",150)
r2 = Robot("Gal",45)

print(r1)
print(r1+r2)

