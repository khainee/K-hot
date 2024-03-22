import time
import datetime
import requests
import urllib.parse

API_URL = 'https://api0.herewallet.app/api/v1/user/hot/claim'
HEADERS = {
    'Host': 'api0.herewallet.app',
    'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjUyMTQxMTAsImRpZCI6ODQ1OTYzOCwiZGV2aWNlIjpudWxsLCJhY2NvdW50X2lkIjoiaTY0NTkwOTc0NDAudGciLCJkZXZpY2VfaWQiOiIwNWJlMjFmOS02Zjg3LTQ1NTYtYWVjNS02MWNkYjNkMjA2YTAiLCJwbGF0Zm9ybSI6InRlbGVncmFtIiwidGltZXN0YW1wIjoxNzEwODMyMjI0LjAsInZpZXdfb25seSI6ZmFsc2V9.oFroXS98xIOMaNxPCjDQtRT-7pxQcPwjiFGWnOyjPtk',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 11; M2010J19SI Build/RKQ1.201004.002) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.119 Mobile Safari/537.36',
    'Content-Type': 'application/json',
    'Network': 'mainnet',
    'Platform': 'telegram',
    'sec-ch-ua-platform': '"Android"',
}

PAYLOAD = {
    "game_state": {
        "refferals": 0,
        "inviter": "khainezay_1.tg",
        "village": "111646.village.hot.tg",
        "last_claim": 1710992560608961300,
        "firespace": 1,
        "boost": 11,
        "storage": 20,
        "balance": 51180
    }
}

def make_post_request():
    headers = HEADERS.copy()  # Copy headers to avoid modifying the original dictionary
    telegram_data = {
        'id': 6459097440,
        'first_name': 'K',
        'last_name': '',
        'language_code': 'en',
        'allows_write_to_pm': True,
        'chat_instance': '-7410836090700338256',  # Additional parameter
        'chat_type': 'sender',  # Additional parameter
        'auth_date': '1710832328',  # Additional parameter
        'hash': '3b83294a563569d35240aaa05893214a750cd24c9992efebe47da36f53c2b1ff'  # Additional parameter
    }
    telegram_data_str = urllib.parse.urlencode({'user': telegram_data})
    print(telegram_data_str)
    headers['Telegram-Data'] = telegram_data_str
    response = requests.post(API_URL, headers=headers, json=PAYLOAD)
    if response.status_code == 200:
        response_data = response.json()
        PAYLOAD['game_state']['last_claim'] = response_data.get('last_claim', PAYLOAD['game_state']['last_claim'])
        PAYLOAD['game_state']['balance'] = response_data.get('hot_in_storage', PAYLOAD['game_state']['balance'])
        print(f"Claim Success. Current Balance is {int(PAYLOAD['game_state']['balance']) / 1000000}")
    else:
        print("Trying again")
        make_post_request()

while True:
    make_post_request()
    time.sleep(PAYLOAD['game_state']['storage'] * 6 * 60)
