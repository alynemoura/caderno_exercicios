# Criando duas matrizes

import numpy as np
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(f"\nMatriz A:\n{A}\n")
print(f"\nMatriz B:\n{B}\n")

# Produto de Matrizes (diferente da multiplicação elemento a elemento)
# Usando o operador @

produto_matricial = A @ B
print(f"\nProduto de A por B:\n\n{produto_matricial}\n")


#Nesse trecho acima, são criadas duas matrizes 2×2 chamadas A e B.
# Em seguida, é realizado o produto matricial entre elas usando o operador @.
# Diferente da multiplicação elemento a elemento (que faz a operação posição por posição),
#  o produto matricial segue as regras da álgebra linear: cada elemento da matriz resultante 
# é obtido multiplicando os elementos de uma linha da primeira matriz pelos elementos de uma coluna 
# da segunda e somando esses produtos. O cálculo do produto é:
# [ [1 * 5 + 2 * 7, 1 * 6 + 2 * 8], [3 * 5 + 4 * 7, 3 * 6 + 4 * 8] ] =
# [[19, 22], [43, 50]]

# Usando np.dot() ao invés de @
produto_matricial = np.dot(A, B)
print(f"Produto de A por B:\n{produto_matricial}\n")

print(f"\nMatriz A:\n{A}\n")
print(f"\nMatriz B:\n{B}\n")

# Element wise
produto_element_wise = A * B
print(f"Multiplicação Element-Wise de A por B:\n{produto_element_wise}")

# Normalmente usamos o produto matricial (@ ou np.dot) quando implementamos
# modelos de Machine Learning ou IA com redes neurais.
# Essa transformações é feita multiplicando a matriz de pesos da camada (W) pelo vetor ou matriz de entradas (X)
# saida = X @ W + bias
# X -> entradas (amostras x features)
# W -> pesos (features x neurônios)
# bias -> deslocamento adicionado depois
# O resultado é uma nova matriz onde cada neurônio combina as entrads por meio de somas ponderadas.

# A multiplicação element-wise (*) é usada em redes neurais, mas em casos específicos, como:
# Hadamard product em algumas arquiteturas (por exemplo,em gates de LSTM?GRU ou ateenção em Transformers);
# Aplicar máscaras ou pesos individuais diretamente em cada elemento.

# Operações com com matrizes NumPy
A = np.array([[20, 10],
              [30, 40]])

B = np.array([[7, 14],
              [4, 3]])

# Soma de matrizes
soma = A + B

# Subtração
subtracao = A - B

# Dividsão elemento a elemento
divisao = A / B

print("Matriz A:\n", A)
print("\nMatriz B:\n", B)
print("\nSoma A + B:\n", soma)
print("\nSubtração A - B:\n", subtracao)
print("\nDivisão A / B:\n", divisao)