# -*- coding: utf-8 -*-

import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/keyboard')
def keyboard():
    dataSend = {
        "type" : "buttons",
        "buttons" : ["시작하기", "도움말"]
    }

    return jsonify(dataSend)

@app.route('/message', methods=['POST'])
def Message():
    dataReceive = request.get_json()
    content = dataReceive['content']

    if content == u"시작하기":
        dataSend = {
            "message" : {
                "text" : " 아직 개발중이라 대답을 잘 못해도 이해해줘 ㅠㅠ"
            }
        }
    elif content == u"도움말":
        dataSend = {
            "message" : {
                "text" : " 이제 곧 정식 버전이 출시될거야. 조금만기다려!"
            }
        }
    elif u"안녕" in content:
        dataSend = {
            "message" : {
                "text" : "안녕?"
            }
        }
    else:
        dataSend = {
            "message" : {
                "text" : "나랑 놀자아~"
            }
        }

    return jsonify(dataSend)

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 5000)
