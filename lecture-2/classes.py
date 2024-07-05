# example 1
class Point():
    # python magic method: has leading and trailing __
    # __init__ is the constructor in python
    def __init__(self, x, y):
        self.x, self.y = x, y

p = Point(3,7)
print(p.x, p.y)

# example 2
class Flight():
    def __init__ (self, capacity):
        self.capacity = capacity
        self.passengers = []
    
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
    
    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)

people = ["Mark", "Steve", "Mary", "Fred", "Stefan"]
for person in people:
    if flight.add_passenger(person):
        print(F"Added {person} to flight.")
    else:
        print(F"{person} is SOL.  No room to fly.")
        
print(flight.passengers)