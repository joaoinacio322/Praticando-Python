renda_mensal = float(input('Digite sua renda mensal: '))
valor_parcela = float(input('Digite o valor da parcela desejada: '))

if renda_mensal > 2000 and valor_parcela <= 0.3 * renda_mensal:
    print('Empréstimo aprovado!')
elif renda_mensal <= 2000:
    print('Emprestimo NEGADO! Renda insuficiente.')
else:
    print('Emprestimo NEGADO! Parcela acima de 30% da renda.')