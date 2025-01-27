class Resistor:

    def __init__(self, name: str, bus1: str, bus2: str, r: float):
        self.name = name
        self.bus1 = bus1
        self.bus2 = bus2
        self.r = r
        self.g = self.calc_g()

    def calc_g(self):
        return 1/self.r