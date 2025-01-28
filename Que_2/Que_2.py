# Constants
G_wire = 0.1  # Wire conductance in Siemens
N = 100 #number of cells
Vin_min, Vin_max = 0, 1  # Vin range in volts
G_min, G_max = 10e-6, 100e-6  # G range in siemens [0,100µS]

# Generate random Vin and G values
np.random.seed(42)  # For reproducibility
Vin = np.random.uniform(Vin_min, Vin_max, N)  # Vin values (0-1V)
G = np.random.uniform(G_min, G_max, N)  # G values (10-100 µS)

# Calculate equivalent conductance
G_sum = np.sum(G)  # Sum of all conductances due to resistor
G_eq = 1 / (1 / G_sum + 1 / G_wire)  # Equivalent conductance

# Calculate Iout_b
Iout_b = G_eq * np.mean(Vin)  # Assuming a single Vin value drives the column

# Verification: Ideal current
I_ideal = np.sum(Vin * G)

# Print results
print(f"G_eq: {G_eq:.6e} S")
print(f"Iout_b: {Iout_b:.6e} A")
print(f"I_ideal: {I_ideal:.6e} A")

# Scatter plot Iout_b vs I_ideal
plt.scatter([I_ideal], [Iout_b], color="green", label="Iout_b vs I_ideal")
plt.xlabel("I_ideal (A)")
plt.ylabel("Iout_b (A)")
plt.title("Scatter Plot: Iout_b vs I_ideal")
plt.legend()
plt.grid(True)
plt.show()

