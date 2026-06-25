import utils
option = None

def primary_ui ():
    while True:
        print('---------- MENU INICIAL ----------')
        print('1. Buscar itens.')
        print('2. Cadastrar itens.')
        print('3. Gerar relatório.')
        print('4. Encerrar programa.')
        limit_option = 4
        chosen_option = utils.test(option, limit_option)
        return chosen_option