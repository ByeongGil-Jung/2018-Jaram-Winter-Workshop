import requests as req
import websocket
import json

import data as d
import translator as t


def connectSlack():
    url = d.Urls.base_url.value + d.Urls.token.value
    url_ws = req.get(url)
    try:
        socket_endpoint = url_ws.json()['url']
        websocket.enableTrace(True)
        ws = websocket.WebSocketApp(socket_endpoint, on_message=on_message)
        ws.run_forever()
    except:
        print('connect error')

def on_message(ws, message):
    message = json.loads(message)
    if 'type' not in message.keys() or message['type'] != 'message':
        return
    print(message)
    res = {
        'channel': message['channel'],
        'type': 'message',
        'text': t.translator(message['text'])
    }
    ws.send(json.dumps(res))