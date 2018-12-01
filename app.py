import config as cfg
import fetch


def format_this(data):
    str = ''
    for item in data:
        str += f"{item['site']} | {item['author']}\n{item['assetId']} | {item['title']}\n{item['publishFromDate']} {item['lastmodified']}\n----------------------------\n"
    return str


url = cfg.config['apis']['default'][0]['url']
filter = cfg.config['apis']['default'][0]['filter']

results = fetch.fetch_data(s_url=url, b_json=True, l_filter=filter)

data = [{'assetId': item['assetId'], 'title': item['title'], 'publishFromDate': item['publishFromDate'],
        'lastmodified': item['lastmodified'], 'site': item['newspaperName'], 'author': item['authorName']} for item in results]

print(format_this(data))
