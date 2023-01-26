import requests


item_id = int(input("input item id: "))
price = int(input("input price in robux: "))

with open('cookie.txt', 'r') as f:
    roblosecurity = f'.ROBLOSECURITY={f.read()}'

csrf = requests.post(url='https://auth.roblox.com/v2/logout', headers={'cookie': roblosecurity})
token = csrf.headers["x-csrf-token"]

getuserid = requests.get(url='https://users.roblox.com/v1/users/authenticated', headers={'cookie': roblosecurity})
user_id = getuserid.json()["id"]

getuaids = requests.get(url=f"https://inventory.roblox.com/v1/users/{user_id}/items/0/{item_id}")
uaids = [i['instanceId'] for i in getuaids.json()['data']]

for i in uaids:
    res = requests.patch(url=f'https://economy.roblox.com/v1/assets/{item_id}/resellable-copies/{i}', json={"price":price}, headers={'accept': 'application/json', 'content-type':'application/json', 'cookie': roblosecurity, 'x-csrf-token': token})
    print(f"successfully listed UAID {i} for {price} robux :)" if res.status_code == 200 else print("fail"))

input(" ")