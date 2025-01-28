import numpy as np
import matplotlib.pyplot as plt

# Constants as per the design
N = 100  # Number of elements
Vin_min, Vin_max = 0, 1  # Vin range in volts
G_min, G_max = 10e-6, 100e-6  # G range in siemens [0,100µS]

# Generate random Vin and G values
np.random.seed(42)  # For reproducibility
Vin = np.random.uniform(Vin_min, Vin_max, N)  # Vin values (0-1V)
G = np.random.uniform(G_min, G_max, N)  # G values (10-100 µS)

# Calculate Iout_a
Iout_a = np.sum(G * Vin)

# Verification: Calculate I_ideal
I_ideal = np.sum(Vin * G)

# Print results
print(f"Iout_a: {Iout_a:.6e} A")
print(f"I_ideal: {I_ideal:.6e} A")

# Plot Iout_a vs I_ideal
plt.scatter([I_ideal], [Iout_a], color="blue", label="Iout_a vs I_ideal")
plt.xlabel("I_ideal (A)")
plt.ylabel("Iout_a (A)")
plt.title("Scatter Plot: Iout_a vs I_ideal")
plt.legend()
plt.grid(True)
plt.show()


