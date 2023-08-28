#Problema
'''Faça um programa que leia um número inteiro N, calcule e mostre o maior quadrado perfeito menor ou igual a N. Por exemplo, se N for igual a 38, o resultado é 36.'''

#Variáveis de entrada
print('--------------------------------------------------')
num = int(input('Digite um número inteiro: '))

for (count) in range (1, num + 1, 1):
    if (count**2 <= num):
        numMaiorQuadradoPerf = count**2

#Saída do programa
print('--------------------------------------------------')
print(f'O maior quadrado perfeito menor ou igual a {num} é {numMaiorQuadradoPerf}.')
print('--------------------------------------------------')