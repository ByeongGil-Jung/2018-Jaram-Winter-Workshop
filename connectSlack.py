import requests as req
import websocket
import json

import data as d
import translator as t


def connectSlack():
    url = d.SlackUrls.base_url.value + d.SlackUrls.token.value
    url_ws = req.get(url)
    try:
        socket_endpoint = url_ws.json()['url']
        websocket.enableTrace(True)
        ws = websocket.WebSocketApp(socket_endpoint, on_message=on_message)
        ws.run_forever()
    except:
        print('connect error')



def on_message(ws, message):
    # print(message)
    message = json.loads(message)

    if 'type' not in message.keys() or message['type'] != 'message':
        return
    if translator_check(message['text']):
        res = {
            'channel': message['channel'],
            'type': 'message',
            'text': t.translator(message['text'])
        }
        ws.send(json.dumps(res))

def translator_check(input):
    if "영한:" in input:
        if input.find("영한:") == 0:
            input = input.split(":")
            if len(input[1]) >= 2:
                return True
    if "한영:" in input:
        if input.find("한영:") == 0:
            input = input.split(":")
            if len(input[1]) >= 2:
                return True
    return False