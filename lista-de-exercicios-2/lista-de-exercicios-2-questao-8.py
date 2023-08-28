#Variáveis de entrada
nome = input('Digite o nome do aluno: ')
nota1 = float(input('Insira a primeira nota: '))
nota2 = float(input('Insira a segunda nota: '))
nota3 = float(input('Insira a terceira nota: '))

#Processamento de dados
notasTotal = 3
media = (nota1 + nota2 + nota3)/notasTotal

#Saída do programa
print (f'Nome do aluno: {nome}')
print (f'Média do aluno: {media:.1f}')