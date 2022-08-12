import requests

response = requests.get('http://universities.hipolabs.com/search?country=Mexico')
data = response.json()

for item in data:
    print(item['name'])
