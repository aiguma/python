import datetime

def chkNow():

    now = datetime.datetime.now()

    nowDate = now.strftime('%Y-%m-%d')
    nowTime = now.strftime('%H:%M:%S')
    print(nowDate)
    print(nowTime)

def chkNowDate():
    now = datetime.datetime.now()

    nowDate = now.strftime('%Y-%m-%d')
    return nowDate

def chkNowTime():
    now = datetime.datetime.now()

    nowTime = now.strftime('%H:%M:%S')
    return nowTime