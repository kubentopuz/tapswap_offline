import requests
import threading
import time
def process_data(auth):
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Connection': 'keep-alive',
        'Content-Length': '357',
        'Content-Type': 'application/json',
        'Host': 'api.tapswap.ai',
        'Origin': 'https://app.tapswap.club',
        'Referer': 'https://app.tapswap.club/',
        'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
        'X-App': 'tapswap_server',
        'X-Bot': 'no',
        'X-Cv': '621',
    }

    json_data = {
        'bot_key': "app_bot_3",
        'init_data': auth,
        'referrer': None,
    }

    response = requests.post('https://api.tapswap.ai/api/account/login', headers=headers, json=json_data)
    print(response.text)

with open('datatapswap.txt', 'r') as file:
            for line in file:
                auth = line.strip().split('|')
                threading.Thread(target=process_data, args=(auth)).start()
            time.sleep(5)
