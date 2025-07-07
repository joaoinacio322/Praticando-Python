while True:
    print('\nOlá! Vamos cadastrar suas credenciais\n')
    usuario = input('Digite um nome de usuário: ')
    senha = input('\nAgora digite uma senha: ')

    if len(usuario) < 5:
        print('\nO nome de usuário deve ter pelo menos 5 caracteres')
        continue
    elif len(senha) < 8:
        print('\nA senha deve ter pelo menos 8 carcateres')
        continue

    print('\nCadastro realizado com sucesso!')
    break