import requests
from modules import assets
clear = lambda: assets.cl()

def infos(api):
    clear()
    print(assets.banner)
    print(f'[>] Code Nitro', end=''); code = str(input(': '))
    clear()

    r = requests.get(f'{api}{code}')

    if r.status_code == 200:
        i = f'''
[Nitro]
Code: {r.json()["code"]}
Uses: {r.json()["uses"]}/{r.json()["max_uses"]}
Expires at: {r.json()["expires_at"]}
Redeemed: {r.json()["redeemed"]}

[Buy by]
Username: {r.json()["user"]["username"]}#{r.json()["user"]["discriminator"]}
ID: {r.json()["user"]["id"]}
        '''
    
    else:
        i = f'\n[>] Invalid or expired nitro'
    return i