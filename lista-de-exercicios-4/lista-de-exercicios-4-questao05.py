#Variáveis constantes
salarioMin = 1212
comissao = 0.05

#Variáveis de entrada
print('-----------------------------------------')
totalVendas = float(input('Informe o valor total das vendas: R$ '))

#Processamento de dados
salarioFunc = totalVendas * comissao

if (salarioFunc < salarioMin):
    salarioFunc = salarioMin

#Saída do programa
print('-----------------------------------------')
print(f'\nSalário do funcionário: R$ {salarioFunc:.2f}')
print('-----------------------------------------')