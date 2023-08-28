#Variáveis de entrada
segs = int(input("Insira um valor (em segundos) para ser convertido: "))

#Processamento de dados
'''
Primeiramente converta o total em segundos para horas
Para tal você precisará pegar apenas a parte inteira para atribuir à variável "horas"
'''
horas = segs//3600
'''
A divisão inteira acima foi feita por 3600 pois em 1h nós temos 60 min, e em 1 min nós temos
60seg, logo 60mins*60segs = 3600segs dentro de 1h
Agora pegue o resto da divisão e atribua aos minutos
'''
minsAux = segs % 3600
'''
Para definir os minutos, basta efetuar a divisão inteira da variável minsAux por 60
A divisão é efetuada por 60 porque agora estamos dentro de minutos e em 1 min temos 60s
'''
mins = minsAux // 60
'''
Já para definir os segundos, resta apenas atribuir o resto da divisão dos minutos à variável segs
'''
segs = minsAux % 60

#Saída do programa
print ("-----------------------------------------------------------")
print (f"VALOR CONVERTIDO = {horas:02}:{mins:02}:{segs:02}.")
print ("-----------------------------------------------------------")
