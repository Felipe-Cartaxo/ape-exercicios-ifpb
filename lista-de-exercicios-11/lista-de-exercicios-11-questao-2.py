import random

#Tamanho da matriz
print('-'*50)
numTam = int(input('Informe o tamanho da matriz: '))
print('-'*50)
numLin = numTam
numCol = numTam

#Inicialização da matriz
matrizA = [None] * numLin
for (countLin) in range (numLin):
  matrizA[countLin] = [None] * numCol

#Geração dos valores da matrizA
print('Elementos da matriz A: ')
print('-'*50)
for (countLin) in range (numLin):
  for (countCol) in range (numCol):
    matrizA[countLin][countCol] = random.randint(1, 10)
    print(f'{matrizA[countLin][countCol]:4}', end='')
  print()
print('-'*50)
#Impressão dos elementos da diagonal
print('Elementos da diagonal principal: ')
print('-'*50)
for (countLin) in range (numLin):
  for (countCol) in range (numCol):
    if (countLin == countCol):
      print(matrizA[countLin][countCol], end= ' ')