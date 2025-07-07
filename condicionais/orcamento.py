orcamento_limite = 3000
despesas = float(input('Digite o total de despesas do mês (R$): '))

if despesas > orcamento_limite:
    print('Atenção! Você ultrapassou o limite do orçamento')
else:
    print(f'PARABÉNS! Você conseguiu economizar e ainda sobrou R$ {orcamento_limite - despesas:.2f}')

