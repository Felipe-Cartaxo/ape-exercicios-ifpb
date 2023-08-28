'''Faça um programa que leia o nome de uma pessoa e exiba-o conforme o exemplo
abaixo.
Obs: Suponha que o nome lido não possua nenhuma preposição, artigo, etc.
Exemplo:
Entrada: FLAVIO RIBEIRO COUTINHO
Saída: COUTINHO, F. R.'''

#Leitura do nome
nome = input('Informe seu nome completo: ').upper()

#Geração do vetor contendo o nome do usuário
vetorNome = nome.split()

#Geração de uma variável auxiliar com o último nome para a variável 'nomeAux'
nomeAux = vetorNome[-1] + ', '

#Leitura do tamanho do vetor
tam = len(vetorNome)

#Leitura das outras partes do nome do usuário (com exceção do último nome)
for (x) in range (tam - 1):
  nomeAux += vetorNome[x][0] + '. '

#Saída do programa
print('-'*50)
print(f'Nome antes da formatação: {nome}')
print(f'Nome formatado: {nomeAux}')