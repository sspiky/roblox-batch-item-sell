import requests

item_id = int(input("input item id: "))
price = int(input("input price in robux: "))

with open('cookie.txt', 'r') as f:
    roblosecurity = f'.ROBLOSECURITY={f.read()}'

token = requests.post(url='https://auth.roblox.com/v2/logout', headers={'cookie': roblosecurity}).headers["x-csrf-token"]
user_id = requests.get(url='https://users.roblox.com/v1/users/authenticated', headers={'cookie': roblosecurity}).json()["id"]
uaids = [i['instanceId'] for i in requests.get(url=f"https://inventory.roblox.com/v1/users/{user_id}/items/0/{item_id}").json()['data']]

for i in uaids:
    res = requests.patch(url=f'https://economy.roblox.com/v1/assets/{item_id}/resellable-copies/{i}', json={"price":price}, headers={'accept': 'application/json', 'content-type':'application/json', 'cookie': roblosecurity, 'x-csrf-token': token})
    print(f"successfully listed UAID {i} for {price} robux :)" if res.status_code == 200 else print("fail"))

input(" ")
