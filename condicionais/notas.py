primeira_nota = float(input('Digite a primeira nota: '))
segundaa_nota = float(input('Digite a segunda nota: '))
terceira_nota = float(input('Digite a terceira nota: '))
media = (primeira_nota + segundaa_nota + terceira_nota) / 3

if media >= 7:
    print('Aprovado!')
elif 5 <= media < 7:
    print('Recuperação')
else:
    print('Reprovado')