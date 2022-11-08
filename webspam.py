import time
import requests
msg = input("Msg: ")
webhook = input("URL: ")
def spam(msg, webhook):
    while True:
        try:
            data = requests.post(webhook, json={'content': msg})
            if data.status_code == 204:
                print(f"Sent MSG {msg}")
        except:
            print("Bad Webhook :" + webhook)
            time.sleep(2)
            exit()
counts = 1
while counts == 1:
    spam(msg, webhook)
