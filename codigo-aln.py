import numpy as np
import matplotlib.pyplot as plt

def analyze_tridiagonal_matrix(T, title):
    eigenvalues, eigenvectors = np.linalg.eigh(T)
    Q = eigenvectors
    
    # Plot eigenvectors (log scale)
    plt.figure()
    for i in [0, 20, 40, 60, 80]:
        plt.semilogy(np.abs(Q[:, i]), label=f'Autovetor {i}')
    plt.title(f'Autovetores de {title} (Escala Log)')
    plt.xlabel('Índice')
    plt.ylabel('Magnitude (log)')
    plt.legend()
    plt.grid(True, which="both", ls="--")
    plt.show()
    
    # Calculate significant entries
    total_entries = Q.size
    significant_entries = np.sum(np.abs(Q) > 1e-10)
    proportion = significant_entries / total_entries
    print(f'Proporção de entradas > 1e-10 em {title}: {proportion:.4f}')

# (a) Matriz aleatória
np.random.seed(0)
n = 100
diag = np.random.randn(n)
subdiag = np.random.randn(n-1)
T_random = np.diag(diag) + np.diag(subdiag, 1) + np.diag(subdiag, -1)
T_random = (T_random + T_random.T)/2  # Garantir simetria

# (b) Laplaciano discreto
T_laplacian = np.diag(-2*np.ones(n)) + np.diag(np.ones(n-1), 1) + np.diag(np.ones(n-1), -1)

analyze_tridiagonal_matrix(T_random, 'Matriz Aleatória')
analyze_tridiagonal_matrix(T_laplacian, 'Laplaciano Discreto')
