import argparse
import ydtrans

KEY_CODE = {
    "APP_KEY": "12e98b67821302c8",
    "SEC_KEY": "EClQZIFpNavmg5Zpx7XRgJk9bHz0fwC5"
}

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument(dest='text', type=str, default='hello', help='a string to translate')
parser.add_argument('-t', '--to', dest='to_lang', type=str,
                    default='auto', help='to language')
parser.add_argument('-f', '--from', dest='from_lang',
                    type=str, default='auto', help='from language')
args = parser.parse_args()

translator = ydtrans.Translator(app_key=KEY_CODE['APP_KEY'],
                                text=args.text,
                                sec_key=KEY_CODE['SEC_KEY'])

translation = translator.translate_text(text=args.text,
                                        from_lang=args.from_lang,
                                        to_lang=args.to_lang,
                                        app_key=KEY_CODE['APP_KEY'])

print translation["translation"][0].encode('utf-8')
