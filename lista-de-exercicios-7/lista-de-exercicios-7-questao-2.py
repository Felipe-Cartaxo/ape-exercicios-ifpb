#Problema
'''Faça um programa que leia vários números, calcule e exiba a média desses números.
Obs: a leitura do número 999 indica o fim dos dados de entrada e não deve ser computado na média)'''

#Declaração de variáveis constantes/de controle

count = 1
numSoma = 0

#Variáveis de entrada
print('---------------------------------------------')
countLimite = int(input('Quantidade de números que serão inseridos: '))
print('---------------------------------------------')

#Processamento de dados
while (count <= countLimite):
    print(f'{count}º nota: ', end='')
    num = float(input(''))
    if (num == 999):
        countLimite = count - 1
        break
    numSoma = numSoma + num
    count = count + 1

numMedia = numSoma/countLimite

#Saída do programa
print('---------------------------------------------')
print(f'A média dos números inseridos é {numMedia:0.1f}.')
print('---------------------------------------------')