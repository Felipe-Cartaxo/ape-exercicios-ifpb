#Variáveis de entrada
print('--------------------------------------------')
nome = input('Informe seu nome: ')
peso = float(input('Informe seu peso (em kg): '))
altura = float(input('Informe seu altura (em m): '))

#Processamento de dados
imc = (peso/(altura**2))

if (imc >= 30):
    grau = 'Obeso mórbido'
elif (imc < 30 and imc >= 26):
    grau = 'Obeso'
else:
    grau = 'Normal'

#Saída do programa
print('--------------------------------------------')
print(f'Nome: {nome}')
print(f'IMC = {imc:0.2f}')
print(f'Grau de obesidade = {grau}')
print('--------------------------------------------')