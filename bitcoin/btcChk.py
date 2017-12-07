import json
import requests

def btcTicker():
    # 코빗 api 이용

    # 비트코인
    req = requests.get(url='https://api.korbit.co.kr/v1/ticker/detailed?currency_pair=btc_krw') # 현재정보
    # print(req.json())

    outVal = json.loads(req.content)

    print("timestamp->", outVal['timestamp'] )
    print("last->", outVal['last'] )
    print("bid->", outVal['bid'] )
    print("ask->", outVal['ask'] )
    print("low->", outVal['low'] )
    print("high->", outVal['high'] )
    print("volume->", outVal['volume'] )
    print("change->", outVal['change'] )
    print("changePercent->", outVal['changePercent'] )
   # print(outVal)

##########################################################

    req2 = requests.get(url='https://api.korbit.co.kr/v1/orderbook') # 매수매도 호가

    outVal2 = json.loads(req2.content)

    #{'timestamp': 1512623002989, 'bids': [['18879500', '2.3731774', '1'], ['18870000', '0.2', '1'], ['18850000', '1.57511662', '1'], ['18849500', '0.00119367', '1'], ['18810000', '0.08', '1'], ['18808500', '0.03', '1'], ['18808000', '0.0011963', '1'], ['18805000', '0.09514379', '1'], ['18802500', '7', '1'], ['18802000', '0.50119669', '1'], ['18801500', '4.5802138', '1'], ['18801000', '0.5023935', '1'], ['18800000', '0.8609503', '1'], ['18799500', '3.00119685', '1'], ['18765000', '0.00119905', '1'], ['18763000', '1.43550247', '1'], ['18762500', '0.1', '1'], ['18762000', '0.00119924', '1'], ['18761500', '0.00119927', '1'], ['18760000', '0.51835474', '1'], ['18750000', '0.26873296', '1'], ['18749500', '0.00120004', '1'], ['18740000', '0.918', '1'], ['18739500', '0.00120068', '1'], ['18702000', '0.10727189', '1'], ['18700000', '3.97659321', '1'], ['18692500', '5.0012037', '1'], ['18691000', '0.00120379', '1'], ['18690000', '0.02675227', '1'], ['18660000', '0.07436891', '1']], 'asks': [['18880000', '0.38523523', '1'], ['18884000', '0.50475477', '1'], ['18884500', '2.98748955', '1'], ['18885000', '0.4', '1'], ['18889000', '0.05252078', '1'], ['18890000', '0.28695817', '1'], ['18896500', '0.09', '1'], ['18899000', '0.0229', '1'], ['18900000', '7.61121496', '1'], ['18909500', '0.05346522', '1'], ['18910000', '1.33297117', '1'], ['18920000', '0.16957037', '1'], ['18925000', '0.003', '1'], ['18944500', '0.01844448', '1'], ['18945000', '0.25649576', '1'], ['18948000', '0.1', '1'], ['18948500', '5.09813443', '1'], ['18950000', '6.16610418', '1'], ['18955500', '0.01487319', '1'], ['18960000', '0.07', '1'], ['18970000', '1.05959701', '1'], ['18975500', '0.274', '1'], ['18980000', '1.81044927', '1'], ['18985000', '0.31133586', '1'], ['18987500', '0.005988', '1'], ['18989000', '0.02229554', '1'], ['18990000', '0.01196193', '1'], ['18998000', '5.03', '1'], ['18999000', '2.28687515', '1'], ['18999500', '0.32460413', '1']]}

    print("outVal2")
    print("timestamp-->", outVal2['timestamp'] )
    print("bids-->", outVal2['bids'] )





    test = 0
    for  bids in outVal2['bids']:
        #print("for bids- ",bids, test)
        for subbids in bids:
            print(test, "sub->", subbids)
        test = test +1

    test = 0
    for asks in outVal2['asks']:
        # print("for asks- ",asks, test)
        for subasks in asks:
            print(test, "sub->", subasks)
        test = test + 1

    #print(outVal2)


##########################################################

    req3 = requests.get(url='https://api.korbit.co.kr/v1/constants') # 제약 조건

    outVal3 = json.loads(req3.content)

    print("minKrwWithdrawal", outVal3['minKrwWithdrawal'])
    print("maxKrwWithdrawal", outVal3['maxKrwWithdrawal'])
    print("krwWithdrawalFee", outVal3['krwWithdrawalFee'])
    print("btcWithdrawalFee", outVal3['btcWithdrawalFee'])
    print("minBtcWithdrawal", outVal3['minBtcWithdrawal'])
    print("maxBtcWithdrawal", outVal3['maxBtcWithdrawal'])
    print("minBtcOrder", outVal3['minBtcOrder'])
    print("maxBtcOrder", outVal3['maxBtcOrder'])
    print("minBtcPrice", outVal3['minBtcPrice'])
    print("maxBtcPrice", outVal3['maxBtcPrice'])
    print("minTradableLevel", outVal3['minTradableLevel'])
    print("btcTickSize", outVal3['btcTickSize'])
    print("minEthOrder", outVal3['minEthOrder'])
    print("maxEthOrder", outVal3['maxEthOrder'])
    print("minEthPrice", outVal3['minEthPrice'])
    print("maxEthPrice", outVal3['maxEthPrice'])
    print("ethTickSize", outVal3['ethTickSize'])
    print("minEtcOrder", outVal3['minEtcOrder'])
    print("maxEtcOrder", outVal3['maxEtcOrder'])
    print("minEtcPrice", outVal3['minEtcPrice'])
    print("maxEtcPrice", outVal3['maxEtcPrice'])
    print("etcTickSize", outVal3['etcTickSize'])

    #print(outVal3)

##########################################################

    req4 = requests.get(url='https://api.coinmarketcap.com/v1/ticker/bitcoin/?convert=KRW') # 비트코인 시세

    outVal4 = json.loads(req4.content)

    for subOutVal4 in outVal4:

        print("id", subOutVal4['id'])
        print("name", subOutVal4['name'])
        print("symbol", subOutVal4['symbol'])
        print("rank", subOutVal4['rank'])
        print("price_usd", subOutVal4['price_usd'])
        print("price_btc", subOutVal4['price_btc'])
        print("24h_volume_usd", subOutVal4['24h_volume_usd'])
        print("market_cap_usd", subOutVal4['market_cap_usd'])
        print("available_supply", subOutVal4['available_supply'])
        print("total_supply", subOutVal4['total_supply'])
        print("max_supply", subOutVal4['max_supply'])
        print("percent_change_1h", subOutVal4['percent_change_1h'])
        print("percent_change_24h", subOutVal4['percent_change_24h'])
        print("percent_change_7d", subOutVal4['percent_change_7d'])
        print("last_updated", subOutVal4['last_updated'])
        print("price_krw", subOutVal4['price_krw'])
        print("24h_volume_krw", subOutVal4['24h_volume_krw'])
        print("market_cap_krw", subOutVal4['market_cap_krw'])

    #print(outVal4)


print(btcTicker())