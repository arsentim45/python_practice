import json

with open('database/data.json') as json_file:
    data = json.load(json_file)
    size = tuple(data['size'])
    subscription_key = data['subscription_key']
    search_url = data['search_url']
    name = data['name']
    count = data['count']