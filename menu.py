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
    
def register_ui ():
    while True:
        print('---------- MENU DE CADASTRO ----------')
        print('1. Cadastrar componentes.')
        print('2. Cadastrar computador.')
        print('3. Retornar ao meu inicial.')
        limit_option = 3
        chosen_option = utils.test(option, limit_option)
        return chosen_option

def hardware_register_ui ():
    print('---------- MENU DE CADASTRO DE COMPONENTES ----------')
    print('1. Cooler.')
    print('2. Gabinete.')
    print('3. Fonte.')
    print('4. HDD ou SSD.')
    print('5. Memória RAM.')
    print('6. Placa mãe.')
    print('7. Placa de vídeo.')
    print('8. Processador.')
    print('9. Retornar ao menu inicial.')
    limit_option = 3
    chosen_option = utils.test(option, limit_option)
    return chosen_option