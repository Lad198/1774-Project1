from VSource import VSource
from Resistor import Resistor
from Load import Load
from Bus import Bus

class Circuit:

    def __init__(self, name: str):
        self.name = name
        self.buses = dict()
        self.resistors = dict()
        self.loads = dict()
        self.vsource = VSource
        self.i = None

# Methods:
    def add_bus(self, bus: str):
        obj = Bus(bus)
        self.buses[bus] = obj

    def add_resistor_element(self, name: str, bus1: str, bus2: str, r: float):
        obj = Resistor(name, bus1, bus2, r)
        self.resistors[name] = obj

    def add_load_element(self, name: str, bus1: str, p: float, v: float):
        obj = Load(name, bus1, p, v)
        self.loads[name] = obj

    def add_vsource_element(self, name: str, bus1: str, v: float):
        obj = VSource(name, bus1, v)
        self.vsource = obj

    def set_i(self, i: float):
        self.i = i

    def print_nodal_voltage(self):
        print("bus ", self.vsource.bus1, " = ", self.vsource.v)
        #converting the dictionary keys to a list
        keys_list = list(self.loads.keys())
        #using the list of keys to print voltage at load
        print("bus ", self.loads[keys_list[0]].bus1, " = ", self.loads[keys_list[0]].v)

    def print_circuit_current(self):
        print("Circuit current = ", self.i)

    #extra method which gives the conductance values
    def get_g_elements(self):
        x=0