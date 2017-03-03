import datetime

now = datetime.datetime.now()
print(now)

nowDate = now.strftime('%Y-%M-%d')
nowTime = now.strftime('%H:%M:%S')
print(nowDate)
print(nowTime)