class Load:

    def __init__(self, name: str, bus1: str, p: float, v: float):
        self.name = name
        self.bus1 = bus1
        self.p = p
        self.v = v
        self.r = v ** 2 / p
        self.g = self.calc_g()

    def calc_g(self):
        return 1 / self.r