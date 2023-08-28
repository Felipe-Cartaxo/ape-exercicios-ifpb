#Problema
'''Escreva um programa para ler 6 números distintos, ou seja, não podem repetir. Exiba os números lidos.'''

#Tamanho do vetor
vetorTam = 6

#Inicialização do vetor
vetor = [None] * vetorTam

#Leitura dos elementos do vetor
for (count) in range (vetorTam):
    while (True):
        vetorAux = int(input(f'Número [{count}]: '))
        existe = False
        
        #Teste para verificar se há um digito igual
        for (countAux) in range (count):
            if (vetorAux == vetor[countAux]):
                existe = True
                break
        if (existe):
            print('Número já existente. Digite novamente.')
            continue

        vetor[count] = vetorAux
        break

#Saída do programa
print(f'Números válidos: {vetor}')