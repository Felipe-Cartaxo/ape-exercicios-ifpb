#Variáveis de entrada
print('------------------------------')
num1 = int(input('1º número inteiro: '))
num2 = int(input('2º número inteiro: '))
num3 = int(input('3º número inteiro: '))

#Processamento de dados
if (num1 > num2 and num1 > num3):
    numMaior = num1
elif (num2 > num3):
    numMaior = num2
else:
    numMaior = num3

#Saída do programa
print('------------------------------')
print(f'O número {numMaior} é o maior.')
print('------------------------------')