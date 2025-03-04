import numpy as np

# Crear una matriz A
A = np.array([[12, -51, 4],
              [6, 167, -68],
              [-4, 24, -41]])

# Realizar la factorización QR
Q, R = np.linalg.qr(A)

# Imprimir los resultados
print("Matriz Q (Ortogonal):")
print(Q)

print("\nMatriz R (Triangular superior):")
print(R)
