atividade_a = int(input('Informe a quantidade de dias para a atividade A:'))
atividade_b = int(input('Informe a quantidade de dias para a atividade B:'))
atividade_c = int(input('Informe a quantidade de dias para a atividade C:'))

if atividade_a < 0 or atividade_b < 0 or atividade_c < 0:
    print('ERRO: os dias não podem ser negativos!')
else:
    tempo_total = atividade_a + atividade_b + atividade_c
    print(f'O tempo total é de {tempo_total} dias')