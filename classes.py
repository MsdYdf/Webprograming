class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        #self.open_seats() == 0
        if not self.open_seats() :  
            return False
        self.passengers.append(name)
        return True

    def open_seats(self)    :
        return self.capacity - len(self.passengers)
    
flight = Flight(3)

people = ['Ali', 'Bardiya', 'Masoud', 'Reza', 'Peyman']
for person in people:
    if flight.add_passenger(person) :
        print(f"added {person} to flight succesfully")
    else:
        print(f'No available seats for {person}')    
    

