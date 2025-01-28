#This directory contains Derivation and Iout_b and its code implementation

Que 2: Calculate Iout for One column resistor Path circuit same as Que 1, but consider wire resistance of Gwire between each cells.

Solution: We can use the principle as the preivous equation. I = G*R; Circuit Conductance: Here, each resistor G(i) is connected with wire of conductance of Gwire. Total equivalent conductance impacted by conductance of resistor and wire resistor.

Iout_b = Vin/Req Iout_b = Vin * Geq Geq = 1/[(1/G1+1/G2+....+1/Gn) + (1/Gwire)]

So, The equation will be: Iout_b = Vin * {1/[(1/G1+1/G2+....+1/Gn) + (1/Gwire)]}
