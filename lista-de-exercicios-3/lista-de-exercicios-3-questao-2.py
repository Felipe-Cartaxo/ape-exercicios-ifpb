#Variáveis constantes
peso1 = 6
peso2 = 4

#Variáveis de entrada
print ("-----------------BOLETIM ONLINE-------------------")
nomeAluno = input("Digite seu nome: ")
nota1 = float(input("Insira sua primeira nota: "))
nota2 = float(input("Insira sua segunda nota:  "))

#Processamento de dados
media = ((nota1 * peso1) + (nota2 * peso2))/(peso1 + peso2)

#Saída do programa
print(f"------------------MEDIA FINAL---------------------")
print(f"NOME DO ALUNO: {nomeAluno}")
print(f"PRIMEIRA NOTA: {nota1}")
print(f"SEGUNDA NOTA:  {nota2}")
print(f"MEDIA:         {media:0.1f}")