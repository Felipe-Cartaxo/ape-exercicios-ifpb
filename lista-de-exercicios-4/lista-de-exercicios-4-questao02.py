#Variáveis de entrada
print('-----------------------------------')
num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))

#Processamento de dados
if (num1 < num2):
    prim = num1
    seg = num2
else:
    prim = num2
    seg = num1

#Saída do programa
print('-----------------------------------')
print(f'Ordem crescente: {prim} ---> {seg}')
print('-----------------------------------')