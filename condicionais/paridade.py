numero =int(input('Digite um número para verificar se é impar ou par: '))

if numero == 0:
    print('O número é ZERO')
elif numero % 2 == 0:
    print('O número é par')
else:
    print('O número é impar')