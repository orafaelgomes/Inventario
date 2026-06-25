def test (option, limit_option):
    try:
        option = int(input(f'\n Escolha entre as opções acima: '))
        if 1 <= option <= limit_option:
            return option
        else: 
            print(f'\nEntrada inválida! Por favor, escolha um número entre 1 e {limit_option} (apenas números são aceitos).\n')
    except ValueError:
        print(f'\nEntrada inválida! Por favor, escolha um número entre 1 e {limit_option} (apenas números são aceitos).\n')