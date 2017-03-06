import nowTime.nowTime as nowTime
import temp.temp as impTemp

def logContent():
    try:
        # 일자별 로그 파일
        # logFile = "log_" + nowTime.logDate() + ".log"

        # f = open("D:\\work\\" + logFile, "a")  # 파일 이어쓰기
        # f = open("D:\\work\\" + logFile, "a") # 파일 이어쓰기

        reVal = ""

        # 날짜 시간 추출
        nowDate = nowTime.chkNowDate()
        nowDate += " " + nowTime.chkNowTime()

        # 기상청 지역 온도 추출
        nowTemp = impTemp.temp()

        reVal = nowDate + "\t" + nowTemp

        # 작성
        # f.write(reVal + "\n")

        # 파일 닫기
        # f.close()

        return reVal

    except FileNotFoundError as e:  # 오류시
        print(e)
