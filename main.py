# coding=utf-8

LANG_CODES = {
    "Chinese Simplified": "zh-CHS",
    "Chinese Traditional": "zh-CHT",
    "English": "EN",
    "French": "fr",
    "Japanese": "ja",
    "Korean": "ko",
    "Portuguese": "pt",
    "Russian": "ru",
    "Spanish": "es"
}

KEY_CODE = {
    "APP_KEY": "12e98b67821302c8",
    "SEC_KEY": "EClQZIFpNavmg5Zpx7XRgJk9bHz0fwC5"
}

LINE_CHAR = 20

import os
import ydtrans
import json

try:
    translator = ydtrans.Translator(
        app_key=KEY_CODE['APP_KEY'],
        text=os.environ['POPCLIP_TEXT'],
        sec_key=KEY_CODE['SEC_KEY'])

    translation = translator.translate_text(
        text=os.environ['POPCLIP_TEXT'],
        from_lang='auto',
        to_lang='auto',
        app_key=KEY_CODE['APP_KEY'])

    # s = json.loads(json.dumps(translation,ensure_ascii=False))
    txt = translation["translation"][0]
    # line = len(txt) / LINE_CHAR + 1
    # if line > 1:
    #     for i in range(line):
    #         if i == 0:
    #             txt = txt[:(LINE_CHAR - 1)] + '\r\n' + txt[(LINE_CHAR - 1):]
    #         else:
    #             txt = txt[:(LINE_CHAR * (i + 1))] + '\r\n' + txt[(LINE_CHAR * (i + 1)):]
    print txt.encode('utf-8')

except Exception as e:
    exit(1)
