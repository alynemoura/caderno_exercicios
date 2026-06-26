# A "vetorização" permite aplicar operações em arrays inteiros de uma só vez, sem a necessidade de loops for, o que é extremamente rápido
import numpy as np
# Simulando dados de preços de produtos
precos = np.array((19.99, 25.50, 8.90, 43.00))
print(f"\nPreços Originais: {precos}\n")

3 # Aplicando um desconto de 10% a todos os preços de uma vez
preco_com_desconto = precos * 0.90
print(f"\nPreços com 10% de desconto: {preco_com_desconto}\n") 

# Mesmo resultado usando Python puro
precos_pp = [19.99, 25.50, 8.90, 43.00]

# Aplicando desconto de 10% usando list comprehension
precos_com_desconto_pp = [precos * 0.90 for preco in precos_pp]
print(f"\nPreços com 10% de desconto: {precos_com_desconto_pp}\n")

# Adicionado um valor fixo de frete
precos_finais = preco_com_desconto + 5.00
print(f"\nPreços Finais com Frete: {precos_finais}\n")

# Usando funções universais (ufuncs) do NumPy
# Exemplo: calculando a raiz quadrada de cada elemento
raizes = np.sqrt(precos)
print(f"\nRaiz Quadrada dos preços: {raizes}")
