#Problema
'''Faça um programa que leia os seguintes dados de um conjunto de alunos: matrícula, nome e as duas notas que ele obteve em suas avaliações. A condição de parada será a digitação de uma matrícula igual 0 (zero). O programa deverá mostrar, para cada aluno, as seguintes informações: matrícula, nome, média e situação (aprovado, se a média for igual ou superior a 7 e, reprovado, se a média for inferior a 7).'''

#Processamento de dados
print('--------------------------------------------------------')
while (True):

    #Variáveis de entrada
    alunoMatri = int(input('Digite sua matricula: '))
    if (alunoMatri == 0):
        print('--------------------------------------------------------')
        print('FIM DO PROGRAMA!')
        print('--------------------------------------------------------')
        break

    alunoNome = input('Digite seu nome: ')
    alunoNota1 = float(input('Digite sua 1ª nota: '))
    alunoNota2 = float(input('Digite sua 2ª nota: '))
    
    alunoMedia = (alunoNota1 + alunoNota2) / 2
    if (alunoMedia >= 7):
        alunoSituacao = 'Aprovado'
    else:
        alunoSituacao = 'Reprovado'

    #Saída do programa
    print('-------------------BOLETIM ONLINE-----------------------')
    print(f'MATRÍCULA DO ALUNO: {alunoMatri}')
    print(f'NOME DO ALUNO: {alunoNome}')
    print(f'MÉDIA DO ALUNO: {alunoMedia:0.2f}')
    print(f'SITUAÇÃO DO ALUNO: {alunoSituacao}')
    print('--------------------------------------------------------')