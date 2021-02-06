#-*- coding: utf-8 -*-
import pytchat
import time

# 추출하고 싶은 단어 있으면 여기 입력, 여러개면 리스트로 만들고 아래 반복문 추가
targetStr = ""
URL = input("URL 입력: ")
chat = pytchat.create(video_id=URL)

# 날짜 형식
tm = time.localtime()
year = str(tm.tm_year)[2:]
month = str(tm.tm_mon)
day = str(tm.tm_mday)
if len(month) == 1: month = '0' + month
if len(day) == 1: day = '0' + day

def getName(name):
    return name
def getMsg(msg):
    return msg
while chat.is_alive():
    for c in chat.get().sync_items():
        name, message = "", ""
        # targetStr이 이름에 있으면 추출
        if targetStr in c.author.name:
            name = getName(c.author.name)
            message = c.message
        # sargetStr이 메세지에 있으면 추출
        elif targetStr in c.message:
            name = getName(c.message)
            message = getMsg(c.message)
        # 원하는 단어가 없으면 넘김
        else:
            continue
        # txt 파일에 저장
        with open("chatList{}{}{}.txt".format(year, month, day), 'a', encoding='UTF-8') as file:
            file.write(f"{c.datetime} [{name}] [{message}]\n")
            print(f"{c.datetime} [{name}] [{message}]\n")
        # print(f"{c.datetime} [{c.author.name}]- {c.message}")
    # print(chat.get().json())
