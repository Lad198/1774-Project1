from Circuit import Circuit
from Solution import Solution

Obj = Circuit("Circuit1")
Obj.add_vsource_element("V1","A",100)
Obj.add_resistor_element("Rab","A","B",5)
Obj.add_load_element("Lb", "B",2000,100)

S = Solution(Obj)
S.do_power_flow()
Obj.print_nodal_voltage()
Obj.print_circuit_current()