distancia_percorrida = float(input('Digite a distância percorrida (Km): '))

if distancia_percorrida <= 100:
    print('Valor do pedágio: R$ 10,00')
elif 100 < distancia_percorrida <= 200:
    print('Valor do pedágio: R$ 20,00')
else:
    print('Valor do pedágio: R$ 30,00')