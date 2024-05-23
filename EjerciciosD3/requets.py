import requests
url='https://api.sampleapis.com/wines/reds'
response = requests.get(url)

if response.status_code == 200:
    datas = response.json()
    for data in datas[:5]:
        print(data)
else:
    print(f"Error: {response.status_code}")