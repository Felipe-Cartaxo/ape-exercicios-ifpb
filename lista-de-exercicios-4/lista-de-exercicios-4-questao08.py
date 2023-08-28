#Variáveis de entrada
print ('----------------------------------------------------------')
num1 = float(input('1º Operando: '))
num2 = float(input('2º Operando: '))
operacao = input('Informe a operação que deseja realizar: ')
print ('----------------------------------------------------------')

#Processamento de dados
if (operacao == '+'):
    resultado = num1 + num2
    print (f'O resultado de {num1} {operacao} {num2} é {resultado:0.1f}')
elif (operacao == '-'):
    resultado = num1 - num2
    print (f'O resultado de {num1} {operacao} {num2} é {resultado:0.1f}')
elif (operacao == 'x' or '*'):
    resultado = num1 * num2
    print (f'O resultado de {num1} {operacao} {num2} é {resultado:0.1f}')
elif (operacao == '/'):
    resultado = num1 ** num2
    print (f'O resultado de {num1} {operacao} {num2} é {resultado:0.1f}')
elif (operacao == '%'):
    resultado = (num1 % 100) * num2
    print (f'O resultado de {num1} {operacao} {num2} é {resultado:0.1f}')
else:
    print ('Operador desconhecido')
print ('----------------------------------------------------------')