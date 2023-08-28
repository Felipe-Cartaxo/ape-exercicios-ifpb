#Problema
'''Faça um programa que leia um número inteiro e determine se ele é par ou ímpar. Ao final, o programa deve perguntar se o usuário deseja continuar (digitar outro número) ou sair. Se o usuário quiser continuar, o programa deve repetir tudo de novo, caso contrário o programa deve ser encerrado.'''

while (True):
    print('-------------------PAR OU ÍMPAR-------------------------')
    
    #Variáveis de entrada
    num = int(input('Digite um número inteiro: '))

    #Processamento de dados
    if (num % 2 == 0):
        numTipo = 'par'
    else:
        numTipo = 'ímpar'
    
    #Saída do programa
    print(f'O número {num} é {numTipo}.')
    print('-------------------------------------------------------')

    print('Deseja continuar o programa? ')
    print('Digite "S" para continuar.')
    print('Digite "N" para encerrar.')
    print('-------------------------------------------------------')
    print('Resposta: ', end='')
    userResposta = input().upper()

    if (userResposta == 'N'):
        print('-------------------------------------------------------')
        print('                    FIM DO PROGRAMA')
        print('-------------------------------------------------------')
        break