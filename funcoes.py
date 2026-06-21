opcao = None
opcao_limite = None

def escolha ():
    try:
        opcao = int(input('Escolha entre as opções acima: '))
        print()
        
        if opcao in range (1,opcao_limite+1):
            return opcao
        else:
            print('ERRO: Opcão inválida!')
    except ValueError:
            print('ERRO: Opcão inválida!')

def menu_principal ():
    print('1. Cadastrar itens.')
    print('2. Listar itens')
    print(f'3. Encerrar programa. \n')
    opcao_limite = 3
    escolha(opcao)

def menu_cadastro():
    print('1. Hardware isolado.')
    print('2. Conjunto.')
    print(f'3. Retornar ao menu anterior. \n')
    opcao_limite = 3
    escolha(opcao)
    
def cadastro_hardware ():
    escolha(opcao)
    
def cadastro_conjunto ():
    
    config_processador = input['Qual o processador desse dispositivo? ']
    config_ram = input['Quanto e qual a voltagem da memória ram? ']
    config_rom = input['Esse dispositivo utiliza HD ou SSD? ']
    config_ram_quant = input['Qual a capacidade de armazenamento? ']
    
    usuario = input['Quem é o usuário deste de dispositivo? ']
    return

def menu_lista ():
    print('1. Exibir lista completa.')
    print('2. Buscar')
    print(f'3. Retornar ao menu anterior. \n')
    opcao_limite = 3
    escolha(opcao)
    
def menu_filtro ():
    print(f'1. Buscar por hardware isolado.')
    print(f'2. Buscar por conjunto.')
    print(f'3. Retornar ao menu anterior. \n')
    opcao_limite = 3
    escolha(opcao)