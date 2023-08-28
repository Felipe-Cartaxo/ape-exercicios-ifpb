#Problema
'''Faça um programa que calcule e mostre o fatorial de um número N, fornecido pelo usuário'''

#Declaração de variáveis
countAux = 1

#Variáveis de entrada
print('-------------------------------------------')
num = int(input('Digite um número inteiro: '))
print('-------------------------------------------')

#Processamento de dados e saída do programa
if (num == 0):
    print(f'{num}! = {countAux}')
else:
    print(f'{num}! = ', end='')
    
    for (count) in range(1, num + 1, 1):
        countAux = countAux * count

        if (count == num):
            print(f'{count}', end='')
        else:
            print(f'{count} x ', end='')
            
    print(f' = {countAux}')
    print('-------------------------------------------')