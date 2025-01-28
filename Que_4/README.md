Que 4: Calculate the Iout_d for 1T1R cell answer the following questions:

Which 1T1R cell type (A or B) helps more to reduce the difference between Iout_d to I_ideal? Why?
Whydoes computation complexity increase when we change cells from perfect resistor to 1T1R cell?
If you have more time, how will you solve this problem numerically? You don't have to consider transistor gate control
Solution:

Each 1T1R cell consists of a transistor that introduces non-linear behavior and a resistor which is in series with transistor. So current will be impacted by both these non-linear and serial resistor conductance

Transistor current(I): for NMOS transistor in saturation; It=K(Vgs-Vth)^2, if Vgs >Vth; Vgs = Voltage across gate to source , Vth= thershold voltage of transistor

Resistor current(Ir) = Vcell/R Total I in cell = It + IR

Iout_d can be eqaluated using KCL;

Iout_d = Summation of Icell(i), where i = 1 to N

Iout_d = Summation of {K(Vgs(i) - Vth)^2 + Vcell(i)/R} , where i = 1 to N


1. Which 1T1R cell type (A or B) helps more to reduce the difference between Iout_d to I_ideal? Why?
Solution: 1T1R cells introduce non-linear behavior because the transistor in each cell limits the current flow based on the voltage across it (e.g., threshold voltage and I-V characteristics). The 1T1R cell type that minimizes the non-linear behavior or provides a more linear resistance/conductance relationship will better match Iout_d with Iideal

Hence, 1T1R Type A may perform better if it has a higher threshold voltage (reducing leakage currents and non-linear effects). 1T1R Type B may perform better if it provides a more consistent resistance/conductance across the operating voltage range.

2. Whydoes computation complexity increase when we change cells from perfect resistor to 1T1R cell?
Solution: With 1T1R computation complexity increases mainly due to non-linear models, Inter-cell interaction, iterative solver

Unlike resistors, the transistor introduces non-linear I-V characteristics that must be modeled. We need to solve non-linear equations, increasing computational load. The transistor behavior in each cell can affect adjacent cells due to shared voltages or wire resistances. Linear equations used for resistor circuits can be solved directly, but 1T1R circuits require iterative numerical solvers (e.g., Newton-Raphson) to handle the non-linear components.

3. If you have more time, how will you solve this problem numerically? You don't have to consider transistor gate control.
I was able to derive the equation and paricially implement the code in given time. I used following approach for it.

Use a simplified transistor model and Combine it with the resistor model in the cell. Then use KCL for each node and incorporating 1T1R in equations After that, Construct the non-linear equations as a system. Solve them using numerical techniques like Newton-Raphson or a circuit simulation tool (e.g., SPICE). Finally Compare numerical results Iout_d with I_ideal
