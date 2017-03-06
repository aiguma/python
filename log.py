import logging
import logging.handlers
import sys

import nowTime.nowTime as nowTime

logFile = "log_" + nowTime.logDate() + ".log"


# logger 인스턴스를 생성 및 로그 레벨 설정
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# formmater 생성
formatter = logging.Formatter('[%(levelname)s|%(filename)s:%(lineno)s] %(asctime)s > %(message)s')



# fileHandler와 StreamHandler를 생성



if sys.platform.startswith('win32'):
    print('window')
    fileHandler = logging.FileHandler("D:\\work\\" + logFile)
elif sys.platform.startswith('linux'):
    print('linux')
    fileHandler = logging.FileHandler("./etc/log/" + logFile)
elif sys.platform.startswith('darwin'):
    print('mac')
    fileHandler = logging.FileHandler("./etc/log/" + logFile)

streamHandler = logging.StreamHandler()

# logging.basicConfig(filename="D:\\work\\" + logFile, level=logging.DEBUG)


# 포맷팅 세팅
fileHandler.setFormatter(formatter)
streamHandler.setFormatter(formatter)

# Handler를 logging에 추가
logger.addHandler(fileHandler)
logger.addHandler(streamHandler)


# streamHandler = logging.StreamHandler()
