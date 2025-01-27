from VSource import VSource
from Resistor import Resistor
from Load import Load
from Bus import Bus
import numpy as np

class Circuit:
    def __init__(self, name: str):
        self.name = name
        self.buses = dict()
        self.resistors = dict()
        self.loads = dict()
        self.vsource = None
        self.i = 0  # Current in the circuit
        self.voltages = {}  # Dictionary to store bus voltages

    # Method to add a bus
    def add_bus(self, bus: str):
        obj = Bus(bus)
        self.buses[bus] = obj

    # Method to add resistor element
    def add_resistor_element(self, name: str, bus1: str, bus2: str, r: float):
        obj = Resistor(name, bus1, bus2, r)
        self.resistors[name] = obj

    # Method to add load element
    def add_load_element(self, name: str, bus1: str, p: float, v: float):
        obj = Load(name, bus1, p, v)
        self.loads[name] = obj

    # Method to add voltage source element
    def add_vsource_element(self, name: str, bus1: str, v: float):
        obj = VSource(name, bus1, v)
        self.vsource = obj

    # Method to set circuit current
    def set_i(self, i: float):
        self.i = i

    # Method to print the nodal voltages at each bus
    def print_nodal_voltage(self):
        for bus, voltage in self.voltages.items():
            print(f"Bus {bus}: Voltage = {voltage} V")

    # Method to print the circuit current
    def print_circuit_current(self):
        print("Circuit current = ", self.i)

    # Extra method to get conductance values
    def get_g_elements(self):
        g_elements = {}
        for resistor in self.resistors.values():
            g_elements[resistor.name] = resistor.g
        return g_elements