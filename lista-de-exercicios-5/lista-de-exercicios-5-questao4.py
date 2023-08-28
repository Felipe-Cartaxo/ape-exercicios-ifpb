#Variáveis de entrada
print('--------------------------------------------------')
horaInicial = int(input('Informe a hora de ínicio da partida: '))
horaFinal = int(input('Informe a hora de final da partida: '))

#Processamento de dados
if (horaFinal > horaInicial):
    duracaoJogo = horaFinal - horaInicial
else:
    duracaoJogo = (24 - horaInicial) + horaFinal

if (duracaoJogo > 24 or duracaoJogo < 24):
    duracaoJogo = 24
#Saída do programa
print('--------------------------------------------------')
print(f'HORA DE ÍNICIO DA PARTIDA:          {horaInicial}h')
print(f'HORA DE FINAL DA PARTIDA:           {horaFinal}h')
print('--------------------------------------------------')
print(f'TEMPO MÁXIMO DE DURAÇÃO DA PARTIDA: {duracaoJogo}h')
print('--------------------------------------------------')