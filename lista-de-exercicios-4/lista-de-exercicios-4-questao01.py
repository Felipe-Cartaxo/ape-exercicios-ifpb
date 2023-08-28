#Variáveis de entrada
print('-------------------------------------')
num = int(input('Digite um número inteiro: '))

#Processamento de dados
if (num % 2 == 0):
    resultado = 'par'
else:
    resultado = 'ímpar'

#Saída do programa
print('-------------------------------------')
print(f'O número {num} é {resultado}.')
print('-------------------------------------')