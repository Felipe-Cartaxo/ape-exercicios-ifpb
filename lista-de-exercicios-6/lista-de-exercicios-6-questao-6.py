#Problema
'''Faça um programa que leia 3 números inteiros (N, X, Y) e mostre todos os números múltiplos de N entre X e Y.'''

#Variáveis de entrada
print('---------------------------------------------------')
numN = int(input('Informe o valor de N: '))
numX = int(input('Informe o valor de X: '))
numY = int(input('Informe o valor de Y: '))

#Processamento de dados e saída do programa
print('---------------------------------------------------')
print(f'Os múltiplos de {numN} entre {numX} e {numY} são: ')

for (count) in range (numX, numY + 1):
    if (count % numN == 0):
        print(f'{count} ', end='')

print()
print('---------------------------------------------------')