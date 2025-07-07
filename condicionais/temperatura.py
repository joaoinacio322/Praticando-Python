temperatura_maxima = 25
temperatura = float(input('Digite a temperatura atual da sala de servidores: '))

if temperatura > temperatura_maxima:
    print('ALERTA! Temperatura acima do permitido.')
else:
    print("Temperatura em conformidade com os padrões, continue monitorando!")
