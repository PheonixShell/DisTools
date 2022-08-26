import requests
from modules import assets
clear = lambda: assets.cl()

def infos(api):
    clear()
    print(assets.banner)
    print(f'[>] Code Invite', end=''); code = str(input(': '))
    clear()

    r = requests.get(f'{api}{code}')

    if r.status_code == 200:
        inviter = r.json().get('inviter')
        if inviter:
            z = f'Username: {r.json()["inviter"]["username"]}#{r.json()["inviter"]["discriminator"]}\nID: {r.json()["inviter"]["id"]}'
        else:
            z = 'Personalised Link'
        
        i = f'''
[Invite]
Code: {r.json()["code"]}
Expiration: {r.json()["expires_at"]}

[Invited By]
{z}

[Guild]
Name: {r.json()["guild"]["name"]}
ID: {r.json()["guild"]["id"]}
Verification: {r.json()["guild"]["verification_level"]}

[Channel]
Name: {r.json()["channel"]["name"]}
ID: {r.json()["channel"]["id"]}  
        '''
    
    else:
        i = '\n[>] Invalid or expired invite'
    return i