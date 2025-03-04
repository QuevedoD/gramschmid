import numpy as np

def gram_schmidt(V):
    """
    Realiza el proceso de Gram-Schmidt sobre una lista de vectores
    para obtener un conjunto de vectores ortogonales.

    :param V: Lista de vectores (2D numpy array).
    :return: Matriz de vectores ortogonales.
    """
    # Inicializamos la lista de vectores ortogonales
    Q = []

    for v in V:
        # Proyección de v sobre los vectores ortogonales previos
        for q in Q:
            v = v - np.dot(v, q) * q
        # Añadimos el vector ortogonal a la lista
        Q.append(v / np.linalg.norm(v))  # Normalizamos el vector

    return np.array(Q)

# Ejemplo de uso:
if __name__ == "__main__":
    # Definir un conjunto de vectores
    V = np.array([[1, 1], [1, -1], [1, 0]])

    # Aplicar el método de Gram-Schmidt
    Q = gram_schmidt(V)

    # Mostrar los resultados
    print("Vectores ortogonales:")
    print(Q)
