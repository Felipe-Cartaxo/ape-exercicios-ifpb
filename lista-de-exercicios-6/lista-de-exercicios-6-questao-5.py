#Problema
'''Faça um programa que, para um grupo de N pessoas (obs: N será lido):
• Leia o sexo (M ou F) de cada pessoa;
• Calcule e escreva o percentual de homens;
• Calcule e escreva o percentual de mulheres.'''

#Declaração de variáveis
sexoPessoasMasc = 0
sexoPessoasFem = 0

#Variáveis de entrada
print('-----------------------------------------')
numTotalPessoas = int(input('Digite o número total de pessoas: '))

#Processamento de dados
for (count) in range (0, numTotalPessoas, 1):
    sexoPessoa = input('Digite o sexo da pessoa ("M" ou "F"): ').upper()
    if (sexoPessoa == 'M'):
        sexoPessoasMasc = sexoPessoasMasc + 1
    else:
        sexoPessoasFem = sexoPessoasFem + 1
    
percPessoasMasc = (sexoPessoasMasc / numTotalPessoas) * 100
percPessoasFem = (sexoPessoasFem / numTotalPessoas) * 100

#Saída do programa
print('-----------------------------------------')
print(f'PERCENTUAL DE HOMENS    = {percPessoasMasc:0.2f}%')
print(f'PERCENTUAL DE MULHERES  = {percPessoasFem:0.2f}%')
print('-----------------------------------------')