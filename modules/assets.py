from modules import invite, nitro, user
import os, platform, time
my_os = platform.system()

#Variables
apiNitro = "https://discordapp.com/api/v9/entitlements/gift-codes/"
apiInvite = "https://discord.com/api/v9/invites/"
apiLookup = "https://lookupguru.herokuapp.com/lookup"

#Function for clean terminal
def cl():
    if my_os == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

#Function to close DisTools
def end():
    print('Exit of DisTools...')
    time.sleep(1)
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
    print(f'{banner}{menu}')
    print(f'[>]', end=''); choice = str(input(' '))

    match choice:
        case '0':
            end()
        case '1':
            print(invite.infos(apiInvite))
            loop(invite.infos, apiInvite)
        case '2':
            print(nitro.infos(apiNitro))
            loop(nitro.infos, apiNitro)
        case '3':
            print(user.infos(apiLookup))
            loop(user.infos, apiLookup)

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

[By Arkane]\t[V.Alpha1]
'''

#BannerMenu
menu = f'''
[>] Infos:
[1] Invite
[2] Nitro
[3] UserID

[0] Exit
'''