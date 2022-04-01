#Module - 여러 변수와 함수를 가지고 있는 집합체
#표준 모듈:파이썬에 내장되어 있음 / 외부 모듈: 다른 사람이 만들어 공개
#import 'module name'
import math
print(math.sin(1))
## math.#라고 쓰면 사용가능한 함수와 변수 보여줌
print(math.floor(2.5)) #내림
print(math.ceil(2.5)) #올림

#from module import anything you want- 가져온 기능은 모듈명 붙이지 않고 사용 가능
from math import sin, cos, tan,floor, ceil
print(sin(1))
from math import *
#module 이름 변경하여 사용
import math as m
print(m.sin(1))

import random
#random(): 0.0<=x<1.0 사이의 값 리턴
print(random.random())
#uniform(min, max): 지정한 범위 사이의 flaot 리턴
print(random.uniform(10, 20))
#randrange(): 지정한 범위 int를 리턴
print(random.randrange(10))
#choice(list):리스트 내부 요소 랜덤 선택
random.choice([1, 2, 3, 4 ,5])
#shuffle(list): 리스트 요소 섞기
random.shuffle([1, 2, 3, 4 ,5])
#sample(list, k=<숫자>): 리스트의 요소 중에 k개를 뽑기
random.sample([1, 2, 3, 4 ,5], k=2)
##sys module
#시스템과 관련된 정보를 가지고 있음
import sys
print(sys.argv) #명령 매개변수 - 프로그램 실행시 추가로 입력하는 값
#컴퓨터 환경과 관련된 정보 출력
#print(sys.getwindowsversion())
print(sys.copyright)
print(sys.version)
sys.exit()

import os
#현재 운영체제, 현재 폴더, 현재 폴더 내부의 요소
print(os.name)
print(os.getcwd())
print(os.listdir())
#폴더를 만들고 제거
os.mkdir("hello")
os.rmdir("hello")
#파일 생성하고 파일 이름 변경
with open("original.txt", "w") as file:
    file.write("hello")
os.rename("original.txt", "new.txt")
#파일 제거
os.remove("new.txt")
#os.unlink("new.txt")
#시스템 명령어 실행


#datetime
import datetime
now = datetime.datetime.now()
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
#strftime() 함수: 시간을 형식에 맞추어 출력 가능
output_a = now.shifttime("%Y.%m.%d %H:$M:$S")
output_b = "{}년 {}월 {}일 {}시 {}분 {}초".format(now.year, now.month, now.day, now.hour, now.minute, now.second)
output_c = now.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초")
#문자열, 리스트 등 앞에 * 붙이면 요소 하나하나가 매개변수로 지정
print(output_a)
print(output_b)
print(output_c)

import datetime
now = datetime.datetime.now()
#특정 시간 이후 시간
after = now + datetime.timedelta(weeks=1, days=1, hours=1, minutes=1, seconds=1)
print(after.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초"))
#특정 시간 요소 교체
output = now.replace(year=(now.year+1))
print(output.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초"))

#time
import time
time.sleep(5)

#urllib - 인터넷 주소 활용 library
from urllib import request
target = request.urlopen("http://google.com")
output = target.read()
print(output)

