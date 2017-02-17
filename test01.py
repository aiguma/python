import win32com.client
import webbrowser
import temp.temp as temp

import testHead




excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = True
wb = excel.Workbooks.Add()
ws = wb.Worksheets("Sheet1")
ws.Cells(1,1).Value = "hello world"


expenses =(
    ["test1", 100001]
    , ["test2", 100002]
    , ["test3", 100003]
    , ["test4", 100004]
    , ["test5", 100005]
    , ["test6", 100006]
    , ["test7", 100007]
)

row = 2
col = 1
val = 1

for item, cost in(expenses):
    ws.Cells(row, 1).Value = item
    ws.Cells(row, 2).Value = cost
    row = row +1

    print(row)
    print(item)
    print(cost)




url = 'http://naver.com'

# MacOS
#chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

# Windows
# chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
# webbrowser.get(chrome_path).open(url)
#
# print(chrome_path)
# print(url)

# 닫기
excel.Application.Quit()



print(temp.temp() )









