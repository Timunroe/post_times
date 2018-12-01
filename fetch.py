import requests
import random


def fetch_data(s_url, b_json=True, l_filter=None):
    print("+++++++++++++\nNow in fetch_data module ...")
    # string s_url
    # boolean b_json whether to return json or text
    # list of strings that are really keys to drill down the dict
    user_agents = [
        'Mozilla/5.0 (Linux; Android 7.1.2; HTC 2Q4R100 Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Mobile Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0.2 Safari/604.4.7',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
    ]
    headers = {'user-agent': random.choice(user_agents)}
    # print(f"Fetch headers: {headers}")
    r = requests.get(s_url, headers=headers)
    if b_json:
        d = r.json()
        if l_filter:
            temp = d
            for item in l_filter:
                # print(item)
                temp = temp[item]
            return temp
        else:
            return d
    else:
        return r.text
