# -*- coding: utf-8 -*-
import urllib.parse
import requests
from TranslateBot import data as d

def translator(input):
    inputtext = input.split(":")
    batype = inputtext[0]
    btext = inputtext[1]

    if batype == "영한":
        blanguage = "en"
        alanguage = "ko"
    elif batype == "한영":
        blanguage = "ko"
        alanguage = "en"
    else:
        return None

    client_id = d.NaverUrls.client_id.value
    client_secret = d.NaverUrls.client_secret.value
    data = {
        'source': blanguage,
        'target': alanguage, 
        'text': btext
    }
    url = "https://openapi.naver.com/v1/papago/n2mt"
    response = requests.post(url, data=data, headers={
        'X-Naver-Client-Id': client_id,
        'X-Naver-Client-Secret': client_secret
    })
    rescode = response.status_code

    if rescode == 200:
        response_body = response.json()
        # print(response_body.decode('utf-8'))
        print(response_body)
        atext = response_body['message']['result']['translatedText']
        return atext
    else:
        print("Error Code:", rescode)
        print("번역실패")
        return None
