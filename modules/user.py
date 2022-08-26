import requests, json
from modules import assets
clear = lambda: assets.cl()

def infos(api):
    clear()
    print(banner.ban)
    print(f'[>] User ID', end=''); uid = str(input(': '))
    clear()
    
    data = '{"loading":true,"input":' + f'"{uid}"' +',"result":null}'
    req = json.loads(data)
    r = requests.post(api, json=req)
    if r.json()["code"] == 200:
        i = f'''
[User]
Username: {r.json()["data"]["username"]}#{r.json()["data"]["discriminator"]}
ID: {r.json()["data"]["id"]}
Bot: {r.json()["data"]["is_bot"]}
Creation: {r.json()["data"]["created_at"]} (Timestamp)

[Avatar]
URL: {r.json()["data"]["avatar"]["url"]}

[Banner]
URL: {r.json()["data"]["banner"]["url"]}
Color: {r.json()["data"]["banner"]["color"]}
		'''
    else:
        i = f'[>] Invalid user id'
    return i