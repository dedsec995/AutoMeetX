from lib.AutoMeet import AutoMeet
import time
import datetime

getTime = str(datetime.datetime.today().time())
currentTime = getTime[:2] + getTime[3:5]
getDay = int(datetime.datetime.today().weekday())


times = [[1000, 1100], [1110, 1210], [1220, 1320]]
ack = [False,False,False]

usrname = "amit.luhar@universal.edu.in"
passwrd = "youknowwho"
AISC = "https://meet.google.com/lookup/ei2m424nnc"
# MCC = "https://meet.google.com/lookup/kacgotnvup"
MCC = "https://meet.google.com/lookup/ctbxphenpe"
DSIP = "https://meet.google.com/lookup/hf4ighuhkl"
ILOC = "https://meet.google.com/lookup/celj2v3g7t" # CSL         amit viniByte
# ILOC = "https://meet.google.com/lookup/bnk2ns26r4" # MIS       uTTu28
DLOC = "https://meet.google.com/lookup/hh4k4bm4g3" # BDA    dedsec995
# DLOC = "https://meet.google.com/lookup/dcq2zdtwyp" # ASSDF  uTTu28 vinibyte

monday = [ILOC, DSIP, AISC]
tuesday = [ILOC, AISC, DSIP]
wednersday = [ILOC, MCC, DLOC]
thursday = [MCC, DLOC, DSIP]
friday = [DLOC, MCC, AISC]

days = [monday, tuesday, wednersday, thursday, friday]




while True:
    getTime = str(datetime.datetime.today().time())
    currentTime = int(getTime[:2] + getTime[3:5])

    day = days[getDay]
    # print(day)
    for i in range(len(times)):
        if times[i][0] <= currentTime < times[i][1]:
            print(day[i])
            if not ack[i]:
                auto = AutoMeet(usrname,passwrd,"{}".format(day[i]))
                auto.automeetX()
                ack[i] = True

    print("HOLD")
    time.sleep(30)

