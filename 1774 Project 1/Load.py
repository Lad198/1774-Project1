class Load:

    def __init__(self, name: str, bus1: str, p: float, q: float):
        self.name = name
        self.bus1 = bus1
        self.p = p
        self.q = q
        self.g = null

    def calc_g(self):
        S = sqrt(self.p**2 + self.q**2)
        pf = self.p / S
        self.g = self.p / (S * pf)