# Constants
V_offset = 0.05  # Voltage offset for the first column
G_wire = 0.1  # Wire conductance in Siemens

# Generate random G and Vin for two columns
G = np.random.uniform(G_min, G_max, (N, 2))  # Nx2 matrix for G
Vin = np.random.uniform(Vin_min, Vin_max, (N, 2))  # Nx2 matrix for Vin

# Effective voltage for the second column
V_eff = Vin[:, 1] - V_offset

# Calculate equivalent conductance for the second column
G_sum_col2 = np.sum(G[:, 1])  # Sum of G values in column 2
G_eq_col2 = 1 / (1 / G_sum_col2 + 1 / G_wire)  # Equivalent conductance for column 2

# Calculate Iout_c
Iout_c = G_eq_col2 * np.mean(V_eff)  # Using mean V_eff to approximate driving voltage

# Verification: Ideal current for column 2
I_ideal_col2 = np.sum(Vin[:, 1] * G[:, 1])

# Print results
print(f"G_eq_col2: {G_eq_col2:.6e} S")
print(f"Iout_c: {Iout_c:.6e} A")
print(f"I_ideal_col2: {I_ideal_col2:.6e} A")

# Scatter plot Iout_c vs I_ideal_col2
plt.scatter([I_ideal_col2], [Iout_c], color="red", label="Iout_c vs I_ideal_col2")
plt.xlabel("I_ideal_col2 (A)")
plt.ylabel("Iout_c (A)")
plt.title("Scatter Plot: Iout_c vs I_ideal_col2")
plt.legend()
plt.grid(True)
plt.show()

