import pandas as pd
import numpy as np
from VSource import VSource
from Resistor import Resistor
from Load import Load
from Bus import Bus
from Circuit import Circuit

class Solution:
    def __init__(self, circuit: Circuit):
        self.circuit = circuit

    def build_conductance_matrix(self):
        # Initializing the required 2x2 matrix
        self.cond_matrix = np.zeros((len(self.circuit.buses), len(self.circuit.buses)))
        # Setting circuit.g
        self.circuit.get_g_elements()
        # Building the matrix
        self.cond_matrix[0,0] = self.circuit.get_g_elements()
        self.cond_matrix[0, 1] = self.circuit.get_g_elements()
        self.cond_matrix[1, 0] = self.circuit.get_g_elements()
        self.cond_matrix[1, 1] = self.circuit.get_g_elements() + self.circuit.loads["Lb"].g
    def do_power_flow(self):
        self.build_conductance_matrix()
        R_matrix = np.linalg.inv(self.cond_matrix)
        self.circuit.set_i(self.circuit.vsource.v/R_matrix[0,0])
        self.circuit.voltages[self.circuit.resistors["Rab"].bus1] = self.circuit.vsource.v
        self.circuit.voltages[self.circuit.resistors["Rab"].bus2] = self.circuit.vsource.v - self.circuit.i * R_matrix[1,1]