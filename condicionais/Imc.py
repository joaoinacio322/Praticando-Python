peso = float(input('\nDigite seu peso (Kg): '))
altura = float(input('\nDigite sua altura (m) : '))
imc = peso / (altura*altura)

print(f'Seu Imc é: {imc:.2f}')

if imc < 18.5:
    print('\nVocê está abaixo do peso')
elif 18.5 <= imc < 25:
    print('\nSeu peso está normal')
else: 
    print('\nVocê está acima do peso')