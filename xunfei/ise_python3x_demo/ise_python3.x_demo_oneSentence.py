#!/usr/bin/python
# -*- coding: UTF-8 -*-
import base64
import hashlib
import json
import time

import requests

def main():
    x_appid = '5c20a8e7'
    api_key = '30039014e1a51e0e72ee7ddc3ac11c8c'
    curTime = str(int(time.time()))
    url = 'http://api.xfyun.cn/v1/service/v1/ise'
    #text = "Actually, he has over a million subscribers."
    text="兑现的是承诺,换来的是北京的绿色。"
    AUDIO_PATH = r'E:\Work\SpeechDXTest\Tencent\xunfei\ise_python3x_demo\lang\zhcn\wav\0000000001.wav'
    with open(AUDIO_PATH, 'rb') as f:
        file_content = f.read()
    base64_audio = base64.b64encode(file_content)
    body = {'audio': base64_audio, 'text': text}
    param = json.dumps({"aue": "raw", "language": "cn", "category": "read_sentence"})
    paramBase64 = str(base64.b64encode(param.encode('utf-8')), 'utf-8')
    m2 = hashlib.md5()
    m2.update((api_key + curTime + paramBase64).encode('utf-8'))
    checkSum = m2.hexdigest()
    x_header = {
                'X-Appid': x_appid,
                'X-CurTime': curTime,
                'X-Param': paramBase64,
                'X-CheckSum': checkSum,
                'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
                }
    req = requests.post(url, data=body, headers=x_header)
    result = req.content.decode('utf-8')
    print(result)
    output=r"E:\Work\SpeechDXTest\Tencent\xunfei\ise_python3x_demo\output\resultNew.txt"
    fw=open(output, 'w+')
    json.dump(result,fw)
    return


if __name__ == '__main__':
    main()
