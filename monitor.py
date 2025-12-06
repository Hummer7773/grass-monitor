import os
import requests

TOKEN = os.environ['BOT_TOKEN']
CHAT_ID = os.environ['CHAT_ID']

def send_alert(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {'chat_id': CHAT_ID, 'text': msg}
    requests.post(url, data=data)

# Пример однократного запуска
send_alert("✅ Скрипт запущен через GitHub Actions")
