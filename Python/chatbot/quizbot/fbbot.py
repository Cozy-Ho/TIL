# -*- coding: utf-8 -*-
#! Python3

from flask import Flask, request
from OpenSSL import SSL
import os, json, requests

app = Flask(__name__)

#--------------------------
#챗봇 클래스
#--------------------------
class ChatBot(object):
    #초기화
    def __init__(self):
        self.FACEBOOK_TOKEN = 'EAAUWniZCXs9ABAEIXXmCwpx4ZBVaknZBRPsK4V7Wlu8zDayKf3qCH9NllChiqqHyeeQ412oeujcWICtYGxGW1B3uhaZATDuIu20zz6TSTIEqm0ZBTJkMmlKX0DyDxIySH2YyXkzZCdniNYLzNTZAFlzRfZBtGOHJE8z3jF83EkZCBqOAZDZD'
        self.VERIFY_TOKEN = 'Check'
        self.FBMAPI = "https://graph.facebook.com/v2.6/me/message"
        self.fbm_processed = []

    #메세지 처리
    def process_fbm(self, payload):
        for sender, msg in self.fbm_events(payload):
            resp = self.gen_response(msg)
            self.fbm_api({"recipient": {"id": sender}, "message": {"text":
            resp}})

    #메세지 생성
    def gen_response(self, msg):
        return msg

    #메세지 이벤트 처리
    def fbm_events(self, payload):
        data = json.loads(payload.decode('utf-8'))

        for event in data["entry"][0]["messaging"]:
            if "message" in event and "text" in event["message"]:
                q = (event["sender"]["id"], event["message"]["seq"])

                if q in self.fbm_processed:
                    continue
                else:
                    self.fbm_processed.append(q)
                    yield event["sender"]["id"], event["message"]["text"]

    #페이스북 API로 메시지 전송
    def fbm_api(self, data):
        r = requests.post(self.FBM_API, params={"access_token":
        self.FACEBOOK_TOKEN}, data = json.dumps(data), headers={'Content-type':
        'application/json'})

        if r.status_code != requests.codes.ok:
            print("fb error:", r.txt)

#검증 함수
@app.route('/', methods=['GET'])
def Verify():
    if request.args.get('hub.verify_token', '') == bot.VERIFY_TOKEN:
        return request.args.get('hub.challenge','')
    else:
        return 'Error, wrong validation token'

#Webhook 함수
@app.route('/', methods=['POST'])
def Webhook():
    payload = request.get_data()
    bot.process_fbm(payload)
    return "ok"

#MAIN 함수
if __name__ == "__main__":
    bot = ChatBot()
    contextSSL = ('server.crt' , 'server.key')
    app.run(host = '0.0.0.0', port = 5000, ssl_context = contextSSL)


