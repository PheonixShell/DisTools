import requests
from modules import assets
clear = lambda: assets.cl()

def infos():
    clear()
    print(assets.banner)
    print(f'[>] Token', end=''); token = str(input(': '))
    clear()

    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    r = requests.get('https://discord.com/api/v9/users/@me', headers=headers)

    if r.status_code == 200:
        phone = r.json().get('phone')
        if phone:
            p = f'Phone: {r.json()["phone"]}'
        else:
            p = 'No'
        
        i = f'''
[Token]
Username: {r.json()['username']}#{r.json()['discriminator']}
ID: {r.json()['id']}
E-mail: {r.json()['email']}
Phone: {p}
2FA : {r.json()['mfa_enabled']}

Token : {token}
        '''
    
    else:
        i = f'[>] Invalid token'
    return i