P = [
    [0.4, 0.5, 0.1],
    [0.3, 0.4, 0.3],
    [0.5, 0.5, 0.0]
]
def matrix_multiply(A, B):
    n = len(A)
    result = [[sum(A[i][k] * B[k][j] for k in range(n))
               for j in range(n)] for i in range(n)]
    return result
P2 = matrix_multiply(P, P)
prob_lib_to_hostel = P2[0][2]
print("--- Transition Matrix P ---")
for row in P:
    print(row)
print("\n--- 2-Step Transition Matrix (P^2) ---")
for row in P2:
    print([round(x, 2) for x in row])
print(
    f"\nFinal Probability (Library -> Hostel in 2 steps): {prob_lib_to_hostel:.2f}")
