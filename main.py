import core.utils as utils

x = utils.SWJTUCalendar("/Users/ghayinanoghaqino/Downloads/学生个人信息-VATUU为途教学信息服务平台.html")
'''
targets = x.calendar()

trs = targets.find_all("tr")
tds = trs[6].find_all("td")

for each in tds:
    text = each.text
    if text != ' ':
        print(each.text)
    else:
        print("None")
'''

