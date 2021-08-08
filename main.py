import requests

headers = {
    "User-Agent": "Prico"
}

response = requests.post("https://httpbin.org/post",
                         headers=headers,
                         params={'a': 5, 'b': 100},
                         json={'username': 'supersecret'}
                         )

if response.ok:
    print('OK')

print(response.text)