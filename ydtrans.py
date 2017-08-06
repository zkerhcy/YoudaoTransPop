import requests
import hashlib
import urllib


class Translator(object):

    def __init__(self, app_key, text, sec_key):
        self.auth_token = self.__get_authentication_token(
            app_key=app_key, text=text, sec_key=sec_key)

    def __get_authentication_token(self, app_key, text, sec_key):
        m = hashlib.md5()
        m.update(app_key + text + '5' + sec_key)
        hex = m.hexdigest()
        return hex

    def translate_text(self, text, from_lang, to_lang, app_key):
        translate_args = {
            'q': text,
            'from': from_lang,
            'to': to_lang,
            'appKey': app_key,
            'salt': '5',
            'sign': self.auth_token
        }
        r = requests.get('https://openapi.youdao.com/api?' +
                         urllib.urlencode(translate_args))
        if r.status_code == requests.codes.ok:
            r.encoding = 'utf-8'
            return r.json()
        else:
            raise Exception('Failed to obtain translation')
