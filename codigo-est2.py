import numpy as np

# Dados originais
X = np.array([3.85, 3.88, 1.46, 3.74, 3.69, 1.19, 3.06, 1.13, 1.11, 2.24, 4.00, 1.99, 2.40, 2.04, 1.31])
Y = np.array([4.95, 6.63, 4.65, 6.03, 5.26, 3.71, 6.06, 5.19, 3.37, 3.71])

# Parâmetros do bootstrap
B = 1000  # Número de reamostras
np.random.seed(42)  # Para reproducibilidade

# Algoritmo bootstrap para X
medianas_bootstrap_X = []
for b in range(B):
    amostra_bootstrap = np.random.choice(X, size=len(X), replace=True)
    mediana_b = np.median(amostra_bootstrap)
    medianas_bootstrap_X.append(mediana_b)

# Algoritmo bootstrap para Y
medianas_bootstrap_Y = []
for b in range(B):
    amostra_bootstrap = np.random.choice(Y, size=len(Y), replace=True)
    mediana_b = np.median(amostra_bootstrap)
    medianas_bootstrap_Y.append(mediana_b)

# Resultados
erro_padrao_X = np.std(medianas_bootstrap_X, ddof=1)
erro_padrao_Y = np.std(medianas_bootstrap_Y, ddof=1)

print("Resultados para X:")
print(f"Mediana original: {np.median(X):.2f}")
print(f"Erro padrão bootstrap: {erro_padrao_X:.4f}")
print(f"5º percentil: {np.percentile(medianas_bootstrap_X, 5):.2f}")
print(f"95º percentil: {np.percentile(medianas_bootstrap_X, 95):.2f}")

print("\nResultados para Y:")
print(f"Mediana original: {np.median(Y):.2f}")
print(f"Erro padrão bootstrap: {erro_padrao_Y:.4f}")
print(f"5º percentil: {np.percentile(medianas_bootstrap_Y, 5):.2f}")
print(f"95º percentil: {np.percentile(medianas_bootstrap_Y, 95):.2f}")
