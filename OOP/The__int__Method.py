class Robot:
    """This class implements a robot"""
    population = 0 #class attribute(like a counter)
    def __init__(self,name,year):
        self.name = name
        self.year = year
        Robot.population +=1
    def __del__(self):
        print("Robot destroyed")
    def setEnergy(self,energy):
        self.energy = energy


r1 = Robot('R1',2026)#instance
r2 = Robot('ben',2026)
print(r1.__doc__)
print(f'robot name: {r1.name}')
print(r1.__dict__)
print(r1.year)
r1.setEnergy(500)
print(r1.energy)
print(getattr(r1,"energy"))
print(r1.__dict__)


print(f'robots alive: {Robot.population}') # counts robots created