'''Um dado material radioativo perde metade de sua massa a cada 50 segundos. Faça um programa que leia uma certa quantidade de massa, em gramas, deste material e imprima o tempo necessário para que sua massa se torne menor que 0.5g.'''

tempo = 0 #tempo dado em segundos
msgFim = 'Fim do programa'

print('-'*50)
numMassa = float(input('Informe (em gramas) a quantidade de massa: '))

while (numMassa >= 0.5):
    numMassa =  numMassa / 2
    tempo = tempo + 50

print('-'*50)
print(f'Tempo: {tempo} segundos')
print(f'Massa final: {numMassa:.2f} g')
print('-'*50)