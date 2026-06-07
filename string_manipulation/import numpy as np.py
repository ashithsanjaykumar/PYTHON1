import numpy as np

# Step 1: Define the Transition Matrix (P)
# P[i][j] is the probability of moving from state i to state j
P = np.array([[0.8, 0.2],  # Row 0: Sunny transitions
              [0.4, 0.6]])  # Row 1: Rainy transitions

# Step 2: Initial state (100% chance of Sunny)
pi_0 = np.array([1, 0])

# Step 3: Number of days into the future
n = 3

# Step 4: Compute P^n using NumPy's optimized linear algebra power function
P_n = np.linalg.matrix_power(P, n)

# Step 5: Compute final state vector (pi_n = pi_0 * P^n)
pi_n = np.dot(pi_0, P_n)

# Output Results
print(f"--- Weather Prediction after {n} days ---")
print(f"Transition matrix (P^{n}):\n{P_n}")
print(f"\nProbability distribution: {pi_n}")
print(f"Probability of Sunny: {pi_n[0]:.4f}")
print(f"Probability of Rainy: {pi_n[1]:.4f}")
