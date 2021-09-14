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
    "APP_KEY": "${your_app_key}",
    "SEC_KEY": "${your_app_secret_key}",
}

import os
import ydtrans
import json

try:
    translator = ydtrans.Translator(app_key=KEY_CODE['APP_KEY'],
                                    text=os.environ['POPCLIP_TEXT'],
                                    sec_key=KEY_CODE['SEC_KEY'])

    translation = translator.translate_text(text=os.environ['POPCLIP_TEXT'],
                                            from_lang='auto',
                                            to_lang='auto',
                                            app_key=KEY_CODE['APP_KEY'])

    # s = json.loads(json.dumps(translation,ensure_ascii=False))
    print translation["translation"][0].encode('utf-8')

except Exception as e:
    exit(1)
