import config as cfg
import db
import fetch
from time import sleep


def process_results(posts, site):
    data = [{'assetId': item['assetId'], 'title': item['title'], 'publishFromDate': item['publishFromDate'],
             'lastmodified': item['lastmodified'], 'site': item['newspaperName'], 'author': item['authorName']} for item in posts]
    db.db_add(data, site)
    sleep(5)


for item in cfg.config['apis']:
    site = item['name']
    url = item['url']
    filter = item['filter']
    results = fetch.fetch_data(s_url=url, b_json=True, l_filter=filter)
    process_results(results, site)
    db.print_format(site)
