import numpy as np

# Criando um array 1D com 12 elementos
dados_sequencias = np.arange(12)
print(f"\nArray original (1D): {dados_sequencias}\n")

# Remodelando para uma matriz 3x4
matrix_3x4 = dados_sequencias.reshape(3,4)
print(f"\nMatriz 3x4:\n {matrix_3x4}")

# Transpondo a matriz (trocanso linhas por colunas)
matriz_transposta = matrix_3x4.T
print(f"\nMatriz Transposta (4x3): \n{matriz_transposta}\n")

# Achatando a matriz de volta para uma array 1D
array_achatado = matriz_transposta.flatten()
print(f"\nArray achatado (1D): {array_achatado}")