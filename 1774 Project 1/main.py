from Circuit import Circuit
from Solution import Solution

# Create the circuit
Obj = Circuit("Circuit1")

# First, add buses before any elements like resistors or loads
Obj.add_bus("A")
Obj.add_bus("B")

# Now, add elements (voltage source, resistors, and loads)
Obj.add_vsource_element("V1", "A", 200)
Obj.add_resistor_element("Rab", "A", "B", 250)
Obj.add_load_element("Lb", "B", 80, 200)

# Solve the power flow
S = Solution(Obj)
S.do_power_flow()

# Print the nodal voltages and circuit current
Obj.print_nodal_voltage()
Obj.print_circuit_current()
