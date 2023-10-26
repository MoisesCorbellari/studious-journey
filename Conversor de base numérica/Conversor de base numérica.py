while True:
    num_int = int(input('Digite um valor para converter: '))
    print('''Escolha uma opção:
       
        [1] Binário
        [2] Octal
        [3] Hexadecimal
        [0] Sair
      
        ''')
    bas_conv = int(input('Digite a opção desejada: '))
    if bas_conv == 1:
        conv = bin(num_int)[2:]
        print('O número {} convertido para a base {} é: {}.'.format(num_int, 'Binário', conv))
    elif bas_conv == 2:
        conv = oct(num_int)[2:]
        print('O número {} convertido para a base {} é: {}.'.format(num_int, 'Octal', conv))
    elif bas_conv == 3:
        conv = hex(num_int)[2:]
        print('O número {} convertido para a base {} é: {}.'.format(num_int, 'Hexadecimal', conv))
    elif bas_conv == 0:
        print('Saindo do programa.')
        break
    else:
        print('OPÇÃO INVÁLIDA!')
        conv = ''
