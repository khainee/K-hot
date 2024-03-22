import time
import datetime
import requests

current_time = datetime.datetime.now()
timestamp = int(current_time.timestamp())


url = 'https://api0.herewallet.app/api/v1/user/hot/claim'
headers = {
    'Host': 'api0.herewallet.app',
    'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjUyMTQxMTAsImRpZCI6ODQ1OTYzOCwiZGV2aWNlIjpudWxsLCJhY2NvdW50X2lkIjoiaTY0NTkwOTc0NDAudGciLCJkZXZpY2VfaWQiOiIwNWJlMjFmOS02Zjg3LTQ1NTYtYWVjNS02MWNkYjNkMjA2YTAiLCJwbGF0Zm9ybSI6InRlbGVncmFtIiwidGltZXN0YW1wIjoxNzEwODMyMjI0LjAsInZpZXdfb25seSI6ZmFsc2V9.oFroXS98xIOMaNxPCjDQtRT-7pxQcPwjiFGWnOyjPtk',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 11; M2010J19SI Build/RKQ1.201004.002) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.119 Mobile Safari/537.36',
    'Content-Type': 'application/json',
    'Network': 'mainnet',
    'Platform': 'telegram',
    'sec-ch-ua-platform': '"Android"',
    }

payload = {"game_state": {"refferals": 0, "inviter": "khainezay_1.tg", "village": "111646.village.hot.tg", "last_claim": 1710992560608961300, "firespace": 1, "boost": 11, "storage": 20, "balance": 51180}}

def make_post_request():
    headers['Telegram-Data'] = f'user=%7B%22id%22%3A6459097440%2C%22first_name%22%3A%22K%22%2C%22last_name%22%3A%22%22%2C%22language_code%22%3A%22en%22%2C%22allows_write_to_pm%22%3Atrue%7D&chat_instance=-7410836090700338256&chat_type=sender&auth_date=1710832328&hash=3b83294a563569d35240aaa05893214a750cd24c9992efebe47da36f53c2b1ff'
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        response_data = response.json()
        payload['game_state']['last_claim'] = response_data['last_claim']
        payload['game_state']['balance'] = response_data['hot_in_storage']
        print(f"Claim Success. Current Balance is {int(payload['game_state']['balance']) / 1000000}")
        
while True:
    make_post_request()
    time.sleep(payload['game_state']['storage'] * 6 * 60)
