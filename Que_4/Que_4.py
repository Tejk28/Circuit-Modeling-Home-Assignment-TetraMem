from scipy.optimize import fsolve
import numpy as np

# Constants
Vth = 0.4  # Threshold voltage for the transistor (example value)
K = 1e-5  # Transistor parameter (example value)
R = 1e3  # Resistor value in the 1T1R cell (example value)

# Non-linear 1T1R cell model (transistor + resistor)
def cell_current(Vin, Vcell):
    if Vcell > Vth:
        Id = K * (Vcell - Vth)**2  # Transistor current
    else:
        Id = 0  # Transistor is off
    return Id + Vcell / R  # Combine with resistor current

# Circuit model with N cells
def circuit_model(V):
    N = len(V)  # Number of cells
    I = np.zeros(N)
    for i in range(N):
        I[i] = cell_current(Vin[i], V[i])  # Current through each cell
    return I - np.sum(I)  # Enforce KCL (example constraint)

# Inputs
N = 10  # Number of cells
Vin = np.random.uniform(0, 1, N)  # Random input voltages
V_initial = np.zeros(N)  # Initial guesses for the cell voltages

# Solve circuit equations
V_solution = fsolve(circuit_model, V_initial)

# Calculate Iout_d
Iout_d = np.sum([cell_current(Vin[i], V_solution[i]) for i in range(N)])
print(f"Iout_d: {Iout_d:.6e} A")

