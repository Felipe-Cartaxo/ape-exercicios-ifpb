#Problema
'''Chico tem 1,50 metros e cresce 2 centímetros por ano, enquanto Zé tem 1,10 metros e cresce 3 centímetros por ano. Faça um programa que calcule e imprima quantos anos serão necessários para que Zé seja maior que Chico.'''

#Declaração de variáveis constantes/de controle

ano = 1
alturaChico = 1.5
alturaZe = 1.1

while (True):
    print(f'-------------------------ANO {ano}-----------------------------')
    print(f'ALTURA DO CHICO: {alturaChico:0.2f}m')
    print(f'ALTURA DO ZÉ: {alturaZe:0.2f}m')

    #Processamento de dados
    alturaChico = alturaChico + 0.02
    alturaZe = alturaZe + 0.03
    ano = ano + 1

    if (alturaZe > alturaChico):
        print(f'-------------------------ANO {ano}-----------------------------')
        print(f'ALTURA DO CHICO: {alturaChico:0.2f}m')
        print(f'ALTURA DO ZÉ: {alturaZe:0.2f}m')
        print('------------------------------------------------------------')
        print(f'Serão necessários {ano} anos para que Zé seja maior do que Chico.')
        print('------------------------------------------------------------')
        break