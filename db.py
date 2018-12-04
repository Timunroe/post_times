from tinydb import TinyDB, Query


def print_format(site):
    db = TinyDB('db.json')
    table = db.table(site)
    results = table.all()
    str = ''
    for item in results:
        str += f"{item['site']} | {item['author']}\n{item['assetId']} | {item['title']}\nPublished {len(item['publishFromDate'])} time(s): {item['publishFromDate']}\nUpdated {len(item['lastmodified'])} time(s): {item['lastmodified']}\n----------------------------\n"
    db.close()
    print(f"===========================\nSITE: {site}")
    print(str)
    return


def db_add(dict_list, site):
    db = TinyDB('db.json')
    table = db.table(site)
    Record = Query()

    for item in dict_list:
        current_record = db.get(Record.assetId == item['assetId'])
        if current_record:
            # record exists
            # append new time to list
            current_record['publishFromDate'].append(item['publishFromDate'])
            # remove duplicates
            new_pub_times = list(set(current_record['publishFromDate']))
            # append new time to list
            current_record['lastmodified'].append(item['lastmodified'])
            # remove duplicates
            new_update_times = list(set(current_record['lastmodified']))
            # update db
            table.update({'publishFromDate': new_pub_times, 'lastmodified': new_update_times}, Record.assetId == item['assetId'])
        else:
            # record doesn't exist
            item['publishFromDate'] = [item['publishFromDate']]
            item['lastmodified'] = [item['lastmodified']]
            table.insert(item)
    db.close()
    pass
