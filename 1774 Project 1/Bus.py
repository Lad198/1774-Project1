class Bus:

    counter = 0

    def __init__(self, name: str):
        self.name = name
        self.v = 0

    def set_bus_v(self, bus_v):
        self.v = bus_v