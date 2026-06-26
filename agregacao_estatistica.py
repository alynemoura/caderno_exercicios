# Calcular estatísticas descritivas de um conjunto de dados é uma tarefa comum e muito otimizada no NumPy
import numpy as np

# Simulando as notas de 3 alunos em 4 provas
notas = np.array([
    [8.5, 7.0, 9.2, 6.5],
    [5.5, 6.8, 7.5, 8.0],
    [9.5, 9.0, 8.8, 10.0]
])

print("\nMatriz de Notas:\n")
print(notas)
print("\nTipo:", type(notas))

# Agregações na matriz inteira
print(f"\nMédia geral da Turma: {notas.mean():.2f}")
print(f"\nNota máxima da Turma: {notas.max()}")
print(f"\nNota mínima da Turma: {notas.min()}")
print(f"\nSoma de todas as notas: {notas.sum()}\n")

# Agregação por eixo(axis)
# Média de cada aluno (agregando nas colunas, axis = 1) arredondando para 2 casas decimais
media_por_aluno = notas.mean(axis=1).round(2)
print(f"\nMédia de cada aluno: {media_por_aluno}\n")

# Média de cada prova (agregando nas linhas, axy=0) arredondando para 2 casas decimais
media_por_prova = notas.mean(axis=0).round(2)
print(f"\nMedia de cada prova: {media_por_prova}")