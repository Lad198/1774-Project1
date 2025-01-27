from Circuit import Circuit
from Solution import Solution

# Create the circuit
Obj = Circuit("Circuit1")

# First, add buses before any elements like resistors or loads
Obj.add_bus("A")
Obj.add_bus("B")

# Now, add elements (voltage source, resistors, and loads)
Obj.add_vsource_element("V1", "A", 100)
Obj.add_resistor_element("Rab", "A", "B", 5)
Obj.add_load_element("Lb", "B", 2000, 100)

# Solve the power flow
S = Solution(Obj)
S.do_power_flow()

# Print the nodal voltages
Obj.print_nodal_voltage()

# Print the circuit current
Obj.print_circuit_current()
