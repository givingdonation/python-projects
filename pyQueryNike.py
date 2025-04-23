from pyquery import PyQuery as pq
import json
import time
import os
c = "\tthese checks returned true: "
blackCheckFail = True
blueCheckFail = True
beigeCheckFail = True


while blackCheckFail or blueCheckFail:
    d = pq(url="https://www.nike.com/t/invincible-3-mens-road-running-shoes-Xrd0px/DR2615-401")


    data = json.loads(d("[type='application/json']").text())

    size10black = data["props"]["pageProps"]["initialState"]["Threads"]["products"]["DR2615-001"]["skus"][9]["skuId"]
    availListBlack = data["props"]["pageProps"]["initialState"]["Threads"]["products"]["DR2615-001"]["availableSkus"]

    size10blue = data["props"]["pageProps"]["initialState"]["Threads"]["products"]["DR2615-401"]["skus"][9]["skuId"]
    availListBlue = data["props"]["pageProps"]["initialState"]["Threads"]["products"]["DR2615-401"]["availableSkus"]
    try:
        size10beige = data["props"]["pageProps"]["initialState"]["Threads"]["products"]["DR2615-000"]["skus"][9]["skuId"]
        availListBeige = data["props"]["pageProps"]["initialState"]["Threads"]["products"]["DR2615-000"]["availableSkus"]
        if beigeCheckFail:
            c += "||beige on " + str(time.time()) + "\n" + str(availListBeige)
            beigeCheckFail = False
            os.system("Xdialog --beep --msgbox \"beige on " + str(time.time()) + "\n" + str(availListBeige) + "\" 0 0")
    except KeyError:
        pass
    

    for i in availListBlue:
        if size10blue == i["skuId"] and blueCheckFail:
            c += "||blue on " + str(time.time()) + "\n" + str(i)
            blueCheckFail = False
            os.system("Xdialog --beep --msgbox \"blue on " + str(time.time()) + "\n" + str(i) + "\" 0 0")

    for i in availListBlack:
        if size10black == i["skuId"] and blackCheckFail:
            if "MEDIUM" == i["level"] or "LOW" == i["level"]:
                c += "||black on " + str(time.time()) + "\n" + str(i)
                blackCheckFail = False
                os.system("Xdialog --beep --msgbox \"black on " + str(time.time()) + "\n" + str(i) + "\" 0 0")
    print(str(time.time()) + c)
    time.sleep(5)

