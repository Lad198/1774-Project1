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