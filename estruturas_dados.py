# Numpy infere o tipo de dados automaticamente
import numpy as np

arr_inteiros = np.array((1, 2, 3))
print("Tipo de dado (inteiros):", arr_inteiros.dtype)

# Numpy infere o tipo de dado automaticamente
arr_float = np.array((1.0, 2.0, 3.0))
print("Tipo de dado (float64):", arr_float.dtype)

# Podemos especificar o tipo de dado durante a criação
arr_float = np.array((1, 2, 3), dtype=np.float64)
print("Tipo de dado (flaot64):", arr_float.dtype)
print("Array float:", arr_float)

# Conversão para int64
arr_int = arr_float.astype(np.int64)
print("Tipo convertido:", arr_int.dtype)
print("Array convertido:", arr_int)