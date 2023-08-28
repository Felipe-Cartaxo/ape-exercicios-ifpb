#Variáveis de entrada
print('-------------------------------------------------------------')
nota1 = float(input('1ª nota: '))
nota2 = float(input('2ª nota: '))

#Processamento e saída de dados
mediaEtapa1 = (nota1 + nota2) / 2

if (mediaEtapa1 >= 7):

    print('-------------------------------------------------------------')
    print(f'Média da 1ª etapa: {mediaEtapa1:.1f}')
    print(f'Você foi aprovado(a) na 1ª etapa.')
    print('-------------------------------------------------------------')
    
    notaEtapa2 = float(input('Nota da 2ª etapa: '))

    if (notaEtapa2 >= 8):
        print('Você foi aprovado(a) no concurso, parabéns!')
    else:
        print('Infelizmente você não foi aprovado(a) no concurso.')
else:
    print('Você não foi aprovado (a) na 1ª etapa.')
print('-------------------------------------------------------------')