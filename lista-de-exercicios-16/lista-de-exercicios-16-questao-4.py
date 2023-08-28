import random

#Função para gerar e ler uma matriz
def gen_matriz (nLin, nCol):
  matriz = [None] * nLin

  for (x) in range (nLin):
    matriz[x] = [None] * nCol
    
  for (x) in range(nLin):
    for (y) in range (nCol):
      matriz[x][y] = random.randint(0, 20)

  return matriz
      
#Função para exibir uma matriz formatada
def print_matriz (matriz):
  nLin = len(matriz)
  nCol = len(matriz[0])
  for (x) in range (nLin):
    for (y) in range (nCol):
      print(f'{matriz[x][y]:4}', end='')
    print()
  print()

#Função para somar as matrizes
def sum_matriz (matrizA, matrizB):
  nLin = len(matrizA)
  nCol = len(matrizA[0])
  
  matrizC = [None] * nLin
  for (x) in range (nLin):
    matrizC[x] = [None] * nCol

  for (x) in range (nLin):
    for (y) in range (nCol):
      matrizC[x][y] = matrizA[x][y] + matrizB[x][y]

  return matrizC
  
#Programa principal
nLin = int(input('Informe o número de linhas: '))
nCol = int(input('Informe o número de colunas: '))
print()

matrizA = gen_matriz(nLin, nCol)
matrizB = gen_matriz(nLin, nCol)

print('-'*50)
print('Matriz A: ')
print('-'*50)
print_matriz(matrizA)
print('-'*50)
print('Matriz B: ')
print('-'*50)
print_matriz(matrizB)
print('-'*50)

matrizC = sum_matriz(matrizA, matrizB)
print('Matriz resultante: ')
print('-'*50)
print_matriz(matrizC)