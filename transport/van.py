import transport.vehicle

class Van(transport.vehicle.Vehicle):
    is_refrigerated = False

    def __init__(self, is_refrigerated):
        self.is_refrigerated = is_refrigerated