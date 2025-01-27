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

    def do_power_flow(self):
        # Initialize bus voltages (start with voltage source voltage)
        self.circuit.voltages = {bus: 0 for bus in self.circuit.buses}
        if self.circuit.vsource:
            self.circuit.voltages[self.circuit.vsource.bus1] = self.circuit.vsource.v

        # Number of buses (nodes)
        n_buses = len(self.circuit.buses)

        # Create the admittance matrix (A) and the right-hand side vector (B)
        A = np.zeros((n_buses, n_buses))
        B = np.zeros(n_buses)

        # Map bus names to indices
        bus_name_to_idx = {bus_name: idx for idx, bus_name in enumerate(self.circuit.buses.keys())}

        # Populate the admittance matrix based on resistors (g = 1/r)
        for resistor in self.circuit.resistors.values():
            bus1_idx = bus_name_to_idx[resistor.bus1]
            bus2_idx = bus_name_to_idx[resistor.bus2]
            g = resistor.g

            # Add conductance to the diagonal
            A[bus1_idx, bus1_idx] += g
            A[bus2_idx, bus2_idx] += g

            # Off-diagonal terms for current flows
            A[bus1_idx, bus2_idx] -= g
            A[bus2_idx, bus1_idx] -= g

        # For each load, update the right-hand side vector B
        for load in self.circuit.loads.values():
            bus_idx = bus_name_to_idx[load.bus1]
            B[bus_idx] = load.p / load.v

        # Incorporate the voltage source constraints
        if self.circuit.vsource:
            vsource_bus_idx = bus_name_to_idx[self.circuit.vsource.bus1]
            # Set the voltage at the voltage source bus
            A[vsource_bus_idx, :] = 0
            A[vsource_bus_idx, vsource_bus_idx] = 1
            B[vsource_bus_idx] = self.circuit.vsource.v

        try:
            # Solve the system of linear equations A * V = B
            voltage_solution = np.linalg.solve(A, B)
        except np.linalg.LinAlgError:
            print("The matrix is singular and the system cannot be solved.")
            return

        # Assign the calculated voltages to the buses
        for i, bus in enumerate(self.circuit.buses.keys()):
            self.circuit.voltages[bus] = voltage_solution[i]

        # Calculate current (example: using voltage difference and resistance)
        total_current = 0
        for resistor in self.circuit.resistors.values():
            bus1_voltage = self.circuit.voltages[resistor.bus1]
            bus2_voltage = self.circuit.voltages[resistor.bus2]
            current = (bus1_voltage - bus2_voltage) / resistor.r
            total_current += abs(current)  # We assume current direction matters

        self.circuit.set_i(total_current)
