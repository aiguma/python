import json
import requests

def xrpTkcker():
    # 코빗 api 이용

    # 리플
    req = requests.get(url='https://api.korbit.co.kr/v1/ticker/detailed?currency_pair=xrp_krw')
    # print(req.json())

    outVal = json.loads(req.content)
    print(outVal)

print(xrpTkcker())