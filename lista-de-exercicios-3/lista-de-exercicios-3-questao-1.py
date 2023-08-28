#Variáveis constantes
salarioPiso = 1000
comissao = 200
percentualVendas = 0.05

#Variáveis de entrada
print("--------------------------------------------------")
nomeFunc = input("Digite seu nome: ")
numCarros = int(input("Insira a quantidade de carros vendidos: "))
valorVenda = float(input("Insira o valor total de suas vendas: R$ "))

#Processamento de dados
salarioTotal = (salarioPiso + comissao * numCarros + percentualVendas * valorVenda)

#Saída do programa
print("------------------CONTRACHEQUE--------------------")
print(f"NOME DO FUNCIONÁRIO:                {nomeFunc}")
print(f"NÚMERO DE CARROS VENDIDOS:          {numCarros}")
print(f"PISO SALARIAL:                      R$ {salarioPiso:0.2f}")
print("----------------------TOTAL-----------------------")
print(f"VALOR TOTAL DO SALÁRIO:             R$ {salarioTotal:0.2f}")
print("--------------------------------------------------")