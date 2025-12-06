import os
import time
import requests

TOKEN = os.environ['BOT_TOKEN']
CHAT_ID = os.environ['CHAT_ID']

def send_alert(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {'chat_id': CHAT_ID, 'text': msg}
    requests.post(url, data=data)

while True:
    result = os.system("pgrep -f grass")
    if result != 0:
        send_alert("🚨 Grass-нода не найдена")
    time.sleep(3600)
