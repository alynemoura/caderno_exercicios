# imports
import numpy as np
import math
import time

# Criando uma lista (vetor) com Numpy de 1 milhão de itens
precos_np = np.random.rand(1_000_000)
#print(type(precos_np))

# Cria uma lista (estrutura de dados padrão em Python puro)
precos_list = list(precos_np)
#print(type(precos_list))

# Operação com Numpy
t0= time.time()
desc = precos_np * 0.90
final  = desc + 5
raiz = np.sqrt(precos_np)
print("Numpy: ", time.time() - t0, "segundos")

# Mesma operação com Python puro
t0 = time.time()
desc = [p * 0.90 for p in precos_list]
final = [p + 5 for p in desc]
raiz = [math.sqrt(p) for p in precos_list]
print("Python puro", time.time() - t0, "segundos")