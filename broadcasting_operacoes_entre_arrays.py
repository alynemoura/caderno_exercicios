# Broadcasting é o mecanismo que permite realizar operações aritiméticas entre arrays de formas (shapes)
# Sem precisar copiar ou replicar manualmente os dados.
# Ele funciona expandindo automaticamente as dimensões de arrays menores para que fiquem maiores.

# Matriz 3x3
import numpy as np
matriz = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(type(matriz))
print(matriz.shape)

# Vetor 1D com 3 elementos
vetor = np.array([10, 20, 30])
print(type(vetor))
print(vetor.shape)

# Queremos somar os valores do vetor aos valores de CADA linha da matriz 
print(matriz)
print(vetor)

# Broadcasting: o vetor é "expandido" para cada linha da matriz:
resultado = matriz + vetor
print("\nMatriz Original: \n", matriz)
print("\nVetor: \n", vetor)
print("\nResultado com broadcasting:\n", resultado)

# Matriz com faturamento de 3 produtos em 4 meses
faturamento = np.array([
    [100, 110, 120, 130], # produto A
    [200, 210, 220, 230], # produto B
    [300, 310, 320, 340] # produto C
])

print(type(faturamento))
print(faturamento.shape)

# Vetor com bônus (incentivo) para cada produto
bonus_por_produto = np.array([5, 10, 15])
print(type(bonus_por_produto))
print(bonus_por_produto.shape)

# Queremos adicionar um bônus a cada valor de faturamento, por linha. Ou seja, todos os itens da primeira linha deve receber o Bônus 5
print("\nFaturamento:\n")
print(faturamento)
print("\nBônus por Produto:\n")
print(bonus_por_produto)


# Poderíamos usar a vetorizção e fazer algo assim:
#faturamento_com_bonus = faturamento + bonus_por_produto
#print(faturamento_com_bonus)

# O NumPy "estica" (broadcast) o vetor bônus para que ele possa ser somada à matriz
# Mas forma 'bonus_por_produto' (3,) é incompativel com (3, 4)
# Para somar, precisamos que tenha a forma (3, 1) para o broadcast funcionar nas colunas
bonus_formatado = bonus_por_produto.reshape(3, 1)
print(bonus_formatado.shape)
print("\nBônus por Produto:\n")
print(bonus_formatado)

# Agora sim 
faturamento_com_bonus = faturamento + bonus_formatado
print("\nFaturamento com Bônus (via Broadcasting):\n")
print(faturamento_com_bonus)
