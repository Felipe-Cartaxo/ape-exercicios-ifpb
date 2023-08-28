#Variáveis de entrada
bitsDesejado = int(input("Insira o valor (em bits) que deseja receber: B$ "))

#Processamento de dados
bitsNota50 = bitsDesejado//50
resto = bitsDesejado%50
bitsNota10 = resto//10
resto = resto%10
bitsNota5 = resto//5
resto = resto%5
bitsNota1 = resto

#Saída do programa
print (f"\n{bitsNota50} nota(s) de B$ 50")
print (f"{bitsNota10} nota(s) de B$ 10")
print (f"{bitsNota5} nota(s) de B$ 5")
print (f"{bitsNota1} nota(s) de B$ 1 \n")