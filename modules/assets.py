import os, platform, time
my_os = platform.system()

#Function for clean terminal
def cl():
    if my_os == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

#Function to close DisTools
def end():
    print('Exit of DisTools...')
    time.sleep(3)
    cl()
    return

#Menu function to choice restart, return main menu or quit after running a module
def loop(x, y):
    print(f'[1] Main Menu - [2] Restart - [3] Exit', end=' \n'); choice = str(input('[>] '))
    match choice:
        case '1':
            start()
        case '2':
            x(y)
        case '3':
            end()

#Function to select module
def start():
    cl()
    print(f'{banner}\n{menu}')
    print(f'[>]', end=''); choice = str(input(' '))

    match choice:
        case '0':
            end()
        

#Banner
banner = f'''
 ██████████    ███          ███████████                   ████         
░░███░░░░███  ░░░          ░█░░░███░░░█                  ░░███         
 ░███   ░░███ ████   █████ ░   ░███  ░   ██████   ██████  ░███   █████ 
 ░███    ░███░░███  ███░░      ░███     ███░░███ ███░░███ ░███  ███░░  
 ░███    ░███ ░███ ░░█████     ░███    ░███ ░███░███ ░███ ░███ ░░█████ 
 ░███    ███  ░███  ░░░░███    ░███    ░███ ░███░███ ░███ ░███  ░░░░███
 ██████████   █████ ██████     █████   ░░██████ ░░██████  █████ ██████ 
░░░░░░░░░░   ░░░░░ ░░░░░░     ░░░░░     ░░░░░░   ░░░░░░  ░░░░░ ░░░░░░

[By Arkane]\t[V.alpha1]
'''

#BannerMenu
menu = f'''
[0] Exit
'''