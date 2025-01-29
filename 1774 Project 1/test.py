from Circuit import Circuit
from VSource import VSource
from Solution import Solution

V2 = VSource("V2", "B", 30)
print(V2.v)

Obj = Circuit("Circuit1")
Obj.add_vsource_element("V1","A",20)
Obj.add_resistor_element("Rab","A","B",5)
Obj.add_load_element("Lb", "B",100,10)
Obj.print_nodal_voltage()

S = Solution(Obj)
S.do_power_flow()


def CHATGPT(self):
    # Initialize the voltage for each bus, starting with the voltage source
    self.circuit.voltages = {bus: 0 for bus in self.circuit.buses}
    if self.circuit.vsource:
        self.circuit.voltages[self.circuit.vsource.bus1] = self.circuit.vsource.v

    # Number of buses
    n_buses = len(self.circuit.buses)

    # Initialize the admittance matrix A (for conductances) and the right-hand side vector B
    A = np.zeros((n_buses, n_buses))
    B = np.zeros(n_buses)

    # Map bus names to indices
    bus_name_to_idx = {bus_name: idx for idx, bus_name in enumerate(self.circuit.buses.keys())}

    # Add resistor elements to the admittance matrix (A)
    for resistor in self.circuit.resistors.values():
        bus1_idx = bus_name_to_idx[resistor.bus1]
        bus2_idx = bus_name_to_idx[resistor.bus2]
        g = resistor.g
        print(g)

        # Add conductance to the diagonal for each bus
        A[bus1_idx, bus1_idx] += g
        print(A[bus1_idx, bus1_idx])
        A[bus2_idx, bus2_idx] += g

        # Off-diagonal elements to account for the resistor between the buses
        A[bus1_idx, bus2_idx] -= g
        A[bus2_idx, bus1_idx] -= g

    # Add loads to the right-hand side vector (B)
    for load in self.circuit.loads.values():
        bus_idx = bus_name_to_idx[load.bus1]
        # Power divided by voltage gives the current at the load bus
        z_matrix = np.linalg.inv(A)
        B[bus_idx] = self.circuit.vsource.v / A[bus1_idx, bus1_idx]
        print(A[bus1_idx, bus1_idx])
        print(B[bus_idx])

    # Incorporate the voltage source constraint (if it exists)
    if self.circuit.vsource:
        vsource_bus_idx = bus_name_to_idx[self.circuit.vsource.bus1]
        # Set the voltage at the voltage source bus to the specified value
        A[vsource_bus_idx, :] = 0
        A[vsource_bus_idx, vsource_bus_idx] = 1
        B[vsource_bus_idx] = self.circuit.vsource.v

    # Solve the linear system A * V = B to find the voltages at each bus
    try:
        voltage_solution = np.linalg.solve(A, B)
    except np.linalg.LinAlgError:
        print("The matrix is singular and the system cannot be solved.")
        return

    # Assign the calculated voltages to each bus
    for i, bus in enumerate(self.circuit.buses.keys()):
        self.circuit.voltages[bus] = voltage_solution[i]

    # Calculate current through each resistor using Ohm's Law
    total_current = 0
    for resistor in self.circuit.resistors.values():
        bus1_voltage = self.circuit.voltages[resistor.bus1]
        bus2_voltage = self.circuit.voltages[resistor.bus2]
        current = A[bus1_idx, bus1_idx]
        total_current += abs(current)  # Use absolute value for current calculation

    # Set the total current in the circuit
    self.circuit.set_i(total_current)

