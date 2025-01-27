class Bus:

    counter = 0

    def __init__(self, name: str):
        self.name = name
        self.v = 0
        self.BusNum = Bus.counter
        Bus.counter = Bus.counter + 1

    def set_bus_v(self, bus_v):
        self.v = bus_v