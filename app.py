#
# Python samples are made with Requests: HTTP BY CHR
#
#you be able to change the number of recipient from app and then 
from flask import Flask, request
from dotenv.main import load_dotenv
import requests
import os
import sys

load_dotenv()

app = Flask(__name__)

url = "ADD YOUR API URL"
headers = {'accept': "application/json", 'cache-control': "no-cache"}


username = os.environ.get('username')
password = os.environ.get('password')
domain = os.environ.get('domain')
sender = os.environ.get('sender')


#####

#SEND_ALERT

@app.route('/alert', methods=['POST'])
def send_sms(message):
    payload_json = {'senders':[sender], 'messages':[message], 'recipients':['09366266161'] }
    response = requests.post(url, headers=headers, auth=(username + '/' + domain, password), json=payload_json)
    print(response.json())



#RELOAD
@app.route('/reload', methods=['POST'])
def reload():
    cmd = [sys.executable] + sys.argv
    os.execvp(cmd[0], cmd)
    return 'API is reloaded'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5024)
