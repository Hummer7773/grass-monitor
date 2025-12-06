import os
import time
import requests

TOKEN = os.environ['8355023485:AAFLNjELSBozG5Nr73c7oyTclJIqqbohrkw']
CHAT_ID = os.environ['6005418870']

def send_alert(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {'chat_id': CHAT_ID, 'text': msg}
    requests.post(url, data=data)

while True:
    result = os.system("pgrep -f grass")
    if result != 0:
        send_alert("🚨 Grass-нода не найдена")
    time.sleep(3600)
