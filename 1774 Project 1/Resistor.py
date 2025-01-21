class Resistor:

    def __init__(self, name: str, bus1: str, bus2: str, r: float):
        self.name = name
        self.bus1 = bus1
        self.bus2 = bus2
        self.r = r
        self.g = None

    def calc_g(self):
        self.g = 1/self.r