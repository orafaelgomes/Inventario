import menu
import utils

while True:
    chosen_option = menu.primary_ui()
    if chosen_option == 1:
        print(f'\nFunção indisponível!\n')
        
    elif chosen_option == 2: 
        chosen_option = menu.register_ui()
        if chosen_option == 1:
            chosen_option = menu.hardware_register_ui()
            if chosen_option == 1:
                print(f'\nFunção indisponível!\n')
            elif chosen_option == 2:
                print(f'\nFunção indisponível!\n')
            elif chosen_option == 3:
                print(f'\nFunção indisponível!\n')
            elif chosen_option == 4:
                print(f'\nFunção indisponível!\n')
            elif chosen_option == 5:
                print(f'\nFunção indisponível!\n')
            elif chosen_option == 6:
                print(f'\nFunção indisponível!\n')
            elif chosen_option == 7:
                print(f'\nFunção indisponível!\n')
            elif chosen_option == 8:
                print(f'\nFunção indisponível!\n')
            elif chosen_option == 9:
                chosen_option = menu.register_ui()
                
        elif chosen_option == 2:
            print(f'\nFunção indisponível!\n')
        elif chosen_option == 3: 
            chosen_option = menu.primary_ui()
        
    elif chosen_option == 3:  
        print(f'\nFunção indisponível!\n')
    elif chosen_option == 4: 
        break