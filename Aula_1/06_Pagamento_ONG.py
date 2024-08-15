km_inicio = int(input(('Digite a kilometragem inicial: ')))
km_final = int(input(('Digite a kilometragem final: ')))
litros = float(input('Digite quantos litros de gasolina foram abastecidos: '))

km_percorridos = km_final - km_inicio
consumo = km_percorridos / litros

#print('A distância percorrida foi de {}'.format(km_percorridos)+' e o consumo foi de {}'.format(consumo)+' litros de gasolina')

print('A distância percorrida foi de',km_percorridos,'e o consumo foi de',consumo,'litros de gasolina')