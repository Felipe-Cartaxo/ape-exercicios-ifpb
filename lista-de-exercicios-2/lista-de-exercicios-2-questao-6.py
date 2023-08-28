#Variáveis de entrada
cotacao = float(input('Insira o valor da cotação do dólar: R$ '))
valorDolar = float(input('Insira o valor em dólar: US$ '))

#Processamento de dados
valorReal = valorDolar*cotacao

#Saída do programa
print(f'O valor convertido em reais é R$ {valorReal:.2f}')