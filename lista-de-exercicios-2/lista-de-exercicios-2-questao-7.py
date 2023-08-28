#Variáveis de entrada
pesoPrato = float(input('Insira o peso do prato (em kg): '))

#Processamento de dados
precoKg = 25
valorPrato = pesoPrato*precoKg

#Saída do programa
print (f'O peso do prato do cliente é {pesoPrato} kg. O valor cobrado será de R$ {valorPrato:.2f}')