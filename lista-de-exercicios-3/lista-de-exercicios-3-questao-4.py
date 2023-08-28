#Variáveis de entrada
hodomAtual = float(input("Hodômetro inicial (em Km): "))
hodomDepois = float(input("Hodômetro final (em Km): "))
combustGasto = float(input("Quantidade gasta de combustível (em L): "))
combustPreco = float(input("Preço do litro do combustível: R$ "))
tanqueCapac = float(input("Capacidade do tanque (em L): "))

#Processamento de dados
hodomRodado = hodomDepois - hodomAtual
consumoMedio = hodomRodado / combustGasto
autonomiaCarro = consumoMedio * tanqueCapac
viagemGasto = combustGasto * combustPreco

#Saída do programa
print("\n-----------------------DADOS DA VIAGEM (ANTES)---------------------------")
print(f"VALOR DO HODÔMETRO ANTES DA VIAGEM:         {hodomAtual:0.2f} Km")
print(f"VALOR DO HODÔMETRO APÓS A VIAGEM:           {hodomDepois:0.2f} Km")
print(f"COMBUSTÍVEL GASTO PARA REALIZAR A VIAGEM:   {combustGasto:0.2f} L")
print(f"PREÇO ATUAL DO COMBUSTÍVEL:                 R$ {combustPreco:0.2f}")
print(f"CAPACIDADE ATUAL DO TANQUE:                 {tanqueCapac:0.2f} L")
print("\n-----------------------DADOS DA VIAGEM (DEPOIS)---------------------------")
print(f"QUILOMETRAGEM RODADA:                       {hodomRodado:0.2f} Km")
print(f"CONSUMO:                                    {consumoMedio:0.2f} Km")
print(f"AUTONOMIA:                                  {autonomiaCarro:0.2f} L")
print(f"CUSTO DA VIAGEM:                            R$ {viagemGasto:0.2f}")
print("----------------------------------------------------------------------------")