import pandas as pd
import numpy as np

from Circuit import Circuit

class Solution:

    def __init__(self, circuit: Circuit):
        self.circuit = circuit

    def do_power_flow(self):
        Va = self.circuit.vsource.v
        keys_list1 = list(self.circuit.loads.keys())
        Vb = self.circuit.loads[keys_list1[0]].v
        Vr = Va - Vb
        keys_list2 = list(self.circuit.resistors.keys())
        I = Vr / self.circuit.resistors[keys_list2[0]].r
        self.circuit.set_i(I)

