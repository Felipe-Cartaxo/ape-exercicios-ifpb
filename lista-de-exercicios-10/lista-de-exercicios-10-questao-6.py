#Problema
'''O Brasil possui 26 estados e 1 distrito federal, totalizando 27 unidades federativas. Escreva um programa que armazene, em um vetor, a sigla de todas as unidades federativas. O programa deverá obter de vários usuários qual é a unidade federativa ele acha mais interessante, informando a respectiva sigla. O programa encerra quando for digitada uma sigla inexistente. Ao final, o programa deverá exibir qual foi a sigla mais votada (considere possibilidade de empate).'''

#Inicialização do vetor
vetorUF = ['AC','AL','AM','AP','BA','CE','DF','ES','GO','MA','MG','MS','MT','PA','PB','PE','PI','PR','RJ','RN','RO','RR','RS','SC','SE','SP','TO']

#Tamanho do vetor
vetorTam = len(vetorUF)
vetorOcorr = [0] * vetorTam

print('-'*50)

#Leitura do voto
while (True):
    voto = input('Digite a UF de sua preferência: ').upper()
    for (count) in range (vetorTam):
        if (vetorUF[count] == voto):
            vetorOcorr[count] = vetorOcorr[count] + 1
            break
    else:
        break

#Definição da UF mais votada
maiorVoto = vetorOcorr[0]

for (count) in range (1, vetorTam):
    if (vetorOcorr[count] > maiorVoto):
        maiorVoto = vetorOcorr[count]

#Saída do programa
print('-'*50)
print('UF mais votada: ')
print('-'*50)

for (count) in range (vetorTam):
    if (vetorOcorr[count] == maiorVoto):
        print(f'{vetorUF[count]} com {vetorOcorr[count]} votos.')

print('-'*50)