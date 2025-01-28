#This directory contains Derivation and Iout_b and its code implementation

Que 3: Now we are considering two columns, and there is also wire conductance between the two columns. Calculate the 2nd column current to ground Iout_c. G is no longer a vector, but a Nx2 matrix.

1: What will happen if the 1st column is not connected to perfect ground, but instead a ground with voltage offset V_offset, assume V_offset = 0.05 V.

Solution:

For column 1: Conductance of resistor = G[i,0] Voltage = Vin[i,0] For column 2: Conductance of resistor = G[i,1] Voltage = Vin[i,1]

Total current is impacted by wire conductance between two columns.

Geq = 1/{[1/summation of G[:;1]] + 1/Gwire}

If column 1 is not connected to perfect ground, Voffset = 0.05V affects the current. Therefore, The new voltage driving the current in column 2 becomes: Veff = Vin<2> - Voffset

Hence, Iout_c = Veff * Geq
