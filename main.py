import time
import datetime
import requests

current_time = datetime.datetime.now()
timestamp = int(current_time.timestamp())


url = 'https://api0.herewallet.app/api/v1/user/hot/claim'
headers = {
    'Host': 'api0.herewallet.app',
    'Connection': 'keep-alive',
    'Content-Length': '0',
    'DeviceId': '05be21f9-6f87-4556-aec5-61cdb3d206a0',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Android WebView";v="122"',
    'sec-ch-ua-mobile': '?1',
    #'Telegram-Data': telegram_data_header,
    'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjUyMTQxMTAsImRpZCI6ODQ1OTYzOCwiZGV2aWNlIjpudWxsLCJhY2NvdW50X2lkIjoiaTY0NTkwOTc0NDAudGciLCJkZXZpY2VfaWQiOiIwNWJlMjFmOS02Zjg3LTQ1NTYtYWVjNS02MWNkYjNkMjA2YTAiLCJwbGF0Zm9ybSI6InRlbGVncmFtIiwidGltZXN0YW1wIjoxNzEwODMyMjI0LjAsInZpZXdfb25seSI6ZmFsc2V9.oFroXS98xIOMaNxPCjDQtRT-7pxQcPwjiFGWnOyjPtk',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 11; M2010J19SI Build/RKQ1.201004.002) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.119 Mobile Safari/537.36',
    'Content-Type': 'application/json',
    'Network': 'mainnet',
    'Platform': 'telegram',
    'sec-ch-ua-platform': '"Android"',
    'Accept': '*/*',
    'Origin': 'https://tgapp.herewallet.app',
    'X-Requested-With': 'mark.via.gp',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://tgapp.herewallet.app/',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'en-US,en;q=0.9'
}
def make_post_request():
    headers['Telegram-Data'] = f'user=%7B%22id%22%3A6459097440%2C%22first_name%22%3A%22K%22%2C%22last_name%22%3A%22%22%2C%22language_code%22%3A%22en%22%2C%22allows_write_to_pm%22%3Atrue%7D&chat_instance=-7410836090700338256&chat_type=sender&auth_date=1710832328&hash=3b83294a563569d35240aaa05893214a750cd24c9992efebe47da36f53c2b1ff'
    payload = {"game_state": {"refferals": 0, "inviter": "khainezay_1.tg", "village": "111646.village.hot.tg", "last_claim": 1710992560608961300, "firespace": 1, "boost": 11, "storage": 20, "balance": 51180}}
    response = requests.post(url, headers=headers, json=payload)
    print(response.text)

while True:
    make_post_request()
    time.sleep(2 * 60 * 60)
