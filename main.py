import time
import datetime
import requests
import urllib.parse

API_URL = 'https://api0.herewallet.app/api/v1/user/hot/claim'
HEADERS = {
    'Host': 'api0.herewallet.app',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 11; M2010J19SI Build/RKQ1.201004.002) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.119 Mobile Safari/537.36',
    'Content-Type': 'application/json',
    'Network': 'mainnet',
    'Platform': 'telegram',
    'sec-ch-ua-platform': '"Android"',
}
DATA_K = {
    "game_state": {
        "refferals": 0,
        "inviter": "khainezay_1.tg",
        "village": "111646.village.hot.tg",
        "last_claim": 1710992560608961300,
        "firespace": 4,
        "boost": 13,
        "storage": 23,
        "balance": 5474508
    }
}
DATA_M = {
    "game_state": {
        "refferals": 1,
        "inviter": "khainezay_1.tg",
        "village": "111646.village.hot.tg",
        "last_claim": 1711111010728183600,
        "firespace": 1,
        "boost": 11,
        "storage": 20,
        "balance": 51180
    }
}

def claim_K():
    headers = HEADERS.copy()
    headers['Authorization'] = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjUyMTQxMTAsImRpZCI6ODQ1OTYzOCwiZGV2aWNlIjpudWxsLCJhY2NvdW50X2lkIjoiaTY0NTkwOTc0NDAudGciLCJkZXZpY2VfaWQiOiIwNWJlMjFmOS02Zjg3LTQ1NTYtYWVjNS02MWNkYjNkMjA2YTAiLCJwbGF0Zm9ybSI6InRlbGVncmFtIiwidGltZXN0YW1wIjoxNzEwODMyMjI0LjAsInZpZXdfb25seSI6ZmFsc2V9.oFroXS98xIOMaNxPCjDQtRT-7pxQcPwjiFGWnOyjPtk'
    headers['Telegram-Data'] = 'user=%7B%22id%22%3A6459097440%2C%22first_name%22%3A%22K%22%2C%22last_name%22%3A%22%22%2C%22language_code%22%3A%22en%22%2C%22allows_write_to_pm%22%3Atrue%7D&chat_instance=-7410836090700338256&chat_type=sender&auth_date=1710832328&hash=3b83294a563569d35240aaa05893214a750cd24c9992efebe47da36f53c2b1ff'
    response = requests.post(API_URL, headers=headers, json=DATA_K)
    response_data = response.json()
    if response.status_code == 200:
        DATA_K['game_state']['last_claim'] = response_data.get('last_claim')
        DATA_K['game_state']['balance'] = response_data.get('hot_in_storage')
        print(f"Claim Success.Current Balance of K is {int(PAYLOAD['game_state']['balance']) / 1000000}")
        time.sleep(7200)
    else:
        print(response_data['detail'])

def claim_M():
    headers = HEADERS.copy()
    headers['Authorization'] = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjU5MjYzMCwiZGlkIjoyNzU3Nzc2LCJkZXZpY2UiOm51bGwsImFjY291bnRfaWQiOiJteW9neWkyMzMxMC50ZyIsImRldmljZV9pZCI6IjMxOTM3YTM4LWNlZmItNDRlOS1iNTM5LTBkNDhlMTY5MjYzNiIsInBsYXRmb3JtIjoidGVsZWdyYW0iLCJ0aW1lc3RhbXAiOjE3MTExMTA5MTcuMCwidmlld19vbmx5IjpmYWxzZX0.DdbQET_Kbc5uBl2IwIi3Mq-ICiq_qGDibogc33lXx2E'
    headers['Telegram-Data'] = 'user=%7B%22id%22%3A6320857317%2C%22first_name%22%3A%22Myo%22%2C%22last_name%22%3A%22Gyi%282%EF%B8%8F%E2%83%A33%EF%B8%8F%E2%83%A33%EF%B8%8F%E2%83%A31%EF%B8%8F%E2%83%A30%EF%B8%8F%E2%83%A3%29%22%2C%22username%22%3A%22myogyi23310%22%2C%22language_code%22%3A%22en%22%2C%22allows_write_to_pm%22%3Atrue%7D&chat_instance=4509688859151364008&chat_type=sender&auth_date=1711110826&hash=8ac1220fa6d1aefc36a83eabdf142ab0e2b8f31abb90faa6602710e1d538ab67'
    #data
    response = requests.post(API_URL, headers=headers, json=DATA_M)
    response_data = response.json()
    if response.status_code == 200:
        DATA_M['game_state']['last_claim'] = response_data.get('last_claim')
        DATA_M['game_state']['balance'] = response_data.get('hot_in_storage')
        print(f"Claim Success.Current Balance of M is {int(PAYLOAD['game_state']['balance']) / 1000000}")
        time.sleep(21600)
    else:
        print(response_data['detail'])

time_k = time.time()
time_m = time.time()

while True:
    current_time = time.time()
    if current_time - time_k >= 7200:
        claim_K()
        time_k = time.time()
    if current_time - time_m >= 21600:
        claim_M()
        time_m = time.time()
