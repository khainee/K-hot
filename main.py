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
        "last_claim": 1713561964600336000,
        "firespace": 2,
        "boost": 11,
        "storage": 21,
        "balance": 1122884
    }
}

def make_post_request():
    headers = HEADERS.copy()  # Copy headers to avoid modifying the original dictionary
    headers['Telegram-Data'] = 'user=%7B%22id%22%3A6459097440%2C%22first_name%22%3A%22K%22%2C%22last_name%22%3A%22%22%2C%22language_code%22%3A%22en%22%2C%22allows_write_to_pm%22%3Atrue%7D&chat_instance=-7410836090700338256&chat_type=sender&auth_date=1710832328&hash=3b83294a563569d35240aaa05893214a750cd24c9992efebe47da36f53c2b1ff'
    response = requests.post(API_URL, headers=headers, json=PAYLOAD)
    if response.status_code == 200:
        response_data = response.json()
        print(response_data)
        PAYLOAD['game_state']['last_claim'] = response_data.get('last_claim', PAYLOAD['game_state']['last_claim'])
        PAYLOAD['game_state']['balance'] = response_data.get('hot_in_storage', PAYLOAD['game_state']['balance'])
        balance = int(requests.post(url= API_URL + '/status', headers=headers, json=PAYLOAD).json()['hot_in_storage']) 
        print(f"Claim Success. Current Balance is {balance}")
    else:
        print(f"Trying again.{response.text}")
        make_post_request()

while True:
    make_post_request()
    time.sleep(3 * 60 * 60)
