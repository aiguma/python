import json
import requests

def btcTicker():
    # 코빗 api 이용

    # 비트코인
    req = requests.get(url='https://api.korbit.co.kr/v1/ticker/detailed?currency_pair=btc_krw')
    # print(req.json())

    outVal = json.loads(req.content)
    print(outVal)

print(btcTicker())