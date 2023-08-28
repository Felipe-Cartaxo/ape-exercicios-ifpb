import random

#Tamanho da matriz
numLin = 2
numCol = 3

#Inicialização das matrizes A e B
matrizA = [None] * numLin
matrizB = [None] * numLin
for (countLin) in range (numLin):
  matrizA[countLin] = [None] * numCol
  matrizB[countLin] = [None] * numCol

#Geração da matriz C
matrizC = [None] * numLin
for (countLin) in range (numLin):
  matrizC[countLin] = [None] * numCol

#Geração de valores para a matrizA
for (countLin) in range (numLin):
  for (countCol) in range (numCol):
    matrizA[countLin][countCol] = random.randint (1, 20)

#Geração de valores para a matrizB
for (countLin) in range (numLin):
  for (countCol) in range (numCol):
    matrizB[countLin][countCol] = random.randint (1, 20)

#Soma das matrizes A e B
for (countLin) in range (numLin):
  for (countCol) in range (numCol):
    matrizC[countLin][countCol] = matrizA[countLin][countCol] + matrizB[countLin][countCol]

#Saída do programa
print('-'*50)
print(f'Matriz A: {matrizA}')
print(f'Matriz B: {matrizB}')
print('-'*50)
print(f'Matriz C: {matrizC}')
print('-'*50)