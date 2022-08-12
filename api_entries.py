import requests

search = 'cat'

response = requests.get('https://api.publicapis.org/entries')
data = response.json()

count = data['count']
entries = data['entries']

def print_item_header(item):
    print(f"API: {item['API']}   Description: {item['Description']}")

open_entries = []

for item in entries:
    if item['Auth'] == "":
        open_entries.append(item)

search_entries = []

for item in open_entries:
    if (search in item['API'].lower()) or (search in item['Description'].lower()):
        search_entries.append(item)

for item in search_entries:
    print_item_header(item)
