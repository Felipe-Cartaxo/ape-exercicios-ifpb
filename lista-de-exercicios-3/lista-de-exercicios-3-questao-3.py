#Variáveis de entrada
num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))

#Saída do programa 1
print("------------TROCA DE NÚMEROS--------------")
print(f"PRIMEIRO NÚMERO DIGITADO: {num1}")
print(f"SEGUNDO NÚMERO DIGITADO:  {num2}")

#Processamento de dados
numAux = num1
num1 = num2
num2 = numAux

#Saída do programa 2
print("--------------APÓS A TROCA-----------------")
print(f"PRIMEIRO NÚMERO DIGITADO: {num1}")
print(f"SEGUNDO NÚMERO DIGITADO:  {num2}")
print("-------------------------------------------")