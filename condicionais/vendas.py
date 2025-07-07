quantidade_macas = int(input('\nDigite a quantidade de maçãs vendidas: '))
quantidade_bananas = int(input('\nAgora digite a quantidade de bananas vendidas: '))

if quantidade_macas == quantidade_bananas:
    print('Houve um empate nas vendas\n')
elif quantidade_bananas > quantidade_macas:
    print('\nBanana vendeu mais\n')    
else:
    print('Maçã vendeu mais!')