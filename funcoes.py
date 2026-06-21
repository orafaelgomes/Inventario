opcao = None
opcao_limite = None
tipo = None
processador_freq = None

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
    print('1. Buscar')
    print('2. Cadastar')
    print('3. Emitir Relatório')
    print(f'4. Encerrar programa, \n')
    opcao_limite = 4
    escolha(opcao)
    
def busca ():
    return

def menu_cadastro():
    print('1. Desktop.')
    print('2. Hardware.')
    print(f'3. Retornar ao menu anterior. \n')
    opcao_limite = 4
    escolha(opcao)
    
def menu_cadastro_desktop():
    print('1. Cadastrar desktop.')
    print('2. Cadastrar notebook.')
    print(f'Retornar ao menu anterior. \n')
    opcao_limite = 1
    escolha (opcao)
    if opcao == 1:
        tipo = 'Desktop'
    elif opcao == 2:
        tipo = 'Notebook'
    return tipo

def menu_armazenamento ():
    print(f'Qual o tipo de armazenamento? \n')
    print('1. HDD')
    print('2. SSD')
    print(f'3. Retornar ao menu anterior. \n')
    opcao_limite = 3
    escolha (opcao)
    armazenamento_quant = input['Qual a capacidade? ']
    print()
    if opcao == 1:
        armazenamento = 'HDD'
    elif opcao == 2:
        armazenamento = 'SSD'
    return armazenamento, armazenamento_quant

def menu_processador ():
    processador = input ['Qual o processador? ']
    processador_freq = input ['Qual a frequência? ']
    return processador, processador_freq

def menu_memoria ():
    try:
        memoria_ddr = input ['Qual DDR da memoria? ']
        if memoria_ddr & (1,2,3,4,5):
            return memoria_ddr
        else:
            print('ERRO: Opcão inválida!')
    except ValueError:
            print('ERRO: Opcão inválida!')
            
    memoria_freq = input ['Qual a frequência? ']
    memoria_quant = input ['Qual a capacidade? ']
    return  memoria_freq,memoria_quant

def cadastro_desktop ():
    tipo = [menu_cadastro_desktop(tipo)]
    armazenamento = [menu_armazenamento(armazenamento)]
    armazenamento_quant = [menu_armazenamento(armazenamento_quant)]
    processador = [menu_processador(processador)]
    processador_freq = [menu_processador(processador_freq)]
    memoria_ddr = [menu_memoria(memoria_ddr)]
    memoria_quant = [menu_memoria(memoria_quant)]
    memoria_freq = [menu_memoria(memoria_freq)]
    usuario = input['Quem é o usuário? ']
    return [tipo, armazenamento, armazenamento_quant, processador, processador_freq, memoria_ddr, memoria_freq, memoria_quant, usuario]

def cadastro_hardware ():
    
    escolha(opcao)
    
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