# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import data as d

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
    encText = urllib.parse.quote(btext)
    data = "source="+blanguage+"&target="+alanguage+"&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()

    if rescode == 200:
        response_body = response.read()
        # print(response_body.decode('utf-8'))
        atext = response_body.decode('utf-8').split('\"')[27]
        return atext
    else:
        print("Error Code:" + rescode)
        print("번역실패")
        return None
