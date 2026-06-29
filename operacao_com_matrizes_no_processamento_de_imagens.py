from PIL import Image
import numpy as np

# Abre a imagem 

img = Image.open("imagem2.png")

# Converte para array NumPy
array_img = np.array(img)

print("\nFormato do array:\n", array_img.shape)
#(altura, largura, 3) -> 3 canais = R,G, B

# Obtendo as dimensões
altura, largura, canais = array_img.shape
print(f"\nAltura: {altura}, Largura: {largura}, Canais: {canais}")

# Separamdp cada canal
R = array_img[:, :, 0] # Canal Vermleho
G = array_img[:, :, 1] # Canal Verde
B = array_img[:, :, 2] # Canal Azul

# Extraindo um dos pixels
print("\nExtraindo um dos pixels:\n", array_img[590, 1287])

# Pixel especifico (ex: linha 590, coluna 1287)
pixel = array_img[590, 1287]
r, g, b = pixel
print(f"\nPixel [617, 1287] -> R={r}, G={g}, B{b}")


# Agora vamos recortar um pedaço da imagem

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# --- Carrega a imagem ---
img = Image.open("imagem2.png")
array_img = np.array(img)

# Obtendo dimensões
altura, largura, canais = array_img.shape
print(f"Altura: {altura}, Largura: {largura}, Canais: {canais}")


# --- Definindo um corte central ---
recorte_h = 280
recorte_w = 400

# Definimos o centro da matriz
centro_y = altura // 2
centro_x = largura // 2

# Calculando limites para o recorte central (operações com matrizes para fatiar a imagem)
y_inicio = centro_y - recorte_h // 2
y_fim = centro_y + recorte_h // 2
x_inicio = centro_x - recorte_w // 2
x_fim = centro_x + recorte_w // 2

# fazendo o slice (fatiamento) no array
corte_central = array_img[y_inicio:y_fim, x_inicio:x_fim]
print(f"\nFormato do recorte: {corte_central.shape}")

# --- Mostra a imagem original e o corte ---

plt.figure(figsize= (10, 5))
plt.subplot(1,2,1)
plt.title("Imagem Original")
plt.imshow(array_img)
plt.axis("off")

plt.subplot(1,2,2)
plt.title("Corte Central")
plt.imshow(array_img)
plt.axis("off")


plt.show()