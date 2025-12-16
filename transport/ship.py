import transport.vehicle

class Ship(transport.vehicle.Vehicle):
    name = ""

    def __init__(self, name):
        self.name = name