class Robot:
    """This class implements a robot"""
    def __init__(self,name,year):
        self.name = name
        self.year = year

#instance
r1 = Robot('R1',2026)
print(r1.__doc__)
print(f'robot name: {r1.name}')
print(r1.__dict__)
