#Create a class Transport with variable type. Create 2 child classes Boat and Bus. Boat having variable capacity, source, destination. Bus has variable seat no source destination. Initialise all the variables of all the classes with constructor. Define show method in transport class to display the type of transport. Define show method in Boat class to display type and in Bus class to display the attributes of the bus. Create 2 objects of both boat and bus.

class Transport:
    def __init__(self, type):
        self.type = type

    def show(self):
        print("Transport Type:", self.type)


class Boat(Transport):
    def __init__(self, type, capacity, source, destination):
        super().__init__(type)
        self.capacity = capacity
        self.source = source
        self.destination = destination

    def show(self):
        print("Transport Type:", self.type)
        print("Capacity:", self.capacity)
        print("Source:", self.source)
        print("Destination:", self.destination)


class Bus(Transport):
    def __init__(self, type, seatno, source, destination):
        super().__init__(type)
        self.seatno = seatno
        self.source = source
        self.destination = destination

    def show(self):
        print("Transport Type:", self.type)
        print("Seat No:", self.seatno)
        print("Source:", self.source)
        print("Destination:", self.destination)


boat1 = Boat("Boat", 100, "Kolkata", "Haldia")
boat2 = Boat("Boat", 150, "Mumbai", "Goa")

bus1 = Bus("Bus", 40, "Kolkata", "Durgapur")
bus2 = Bus("Bus", 50, "Delhi", "Jaipur")


print("----- Boat 1 -----")
boat1.show()

boat2.show()

bus1.show()

bus2.show()