import feedparser


def temp():
    # 기상청 날씨 정보 RSS  http://www.kma.go.kr/weather/lifenindustry/sevice_rss.jsp
    feed = feedparser.parse('http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1123061000')

    # 필요부분 추출
    summary = feed['entries'][0]['summary']

    tempSt = summary.find('<temp>')
    tempEn = summary.find('</temp>')

    nowTemp = summary[tempSt + 6:tempEn]

    print('현재온도 : ' + nowTemp)
    return nowTemp

#print(temp())
