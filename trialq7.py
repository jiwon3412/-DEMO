#datetime
import datetime
now = datetime.datetime.now()
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
#strftime() 함수: 시간을 형식에 맞추어 출력 가능
output_a = now.strftime("%Y.%m.%d %H:$M:$S")
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
#urlopen이 사이트 들어감. read 호출하면 해당 웹 페이지 내용 가져옴.

import os
output = os.listdir(".")
print(output)

#현재 폴더 내부의 폴더/파일 구분
for path in output:
    if os.path.isdir(path):
        print("folder:", path)
    else:
        print("file:", path)
#if folder- 탐색하기
def read_folder(path):
    output=os.listdir(path)
    for item in output:
        if os.path.isdir(item):
            read_folder(path+"/"+item)
        else:
            print("file:", item)
read_folder(".") #현재 폴더 파일 출력

#외부 모듈
#pip install 'module_name'- terminal에서 실행
#example:beautiful Soup module (웹 페이지 분석 모듈)# 여러 모듈 - 관심 분야에 따라 다름

#웹개발:Django, Flask
#tensorflow module - 딥러닝에 관련된 모듈
#크롤러 개발: BeautifulSoup, requests, scrapy

#library: 정상적인 제어를 하는 모듈
#framework: 제어역전이 발생하는 모듈
#제어 역전: inversion of control
#library: 개발자가 모듈의 기능을 호출
from math import sin, cos, tan, floor, ceil
print(sin(1))
#framework
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "<h1>Hello World!<h1>"
#외부 터미널에서 set FLASK_APP=flask_basic.py
# flask run
#Flask 모듈 내부에서 서버를 실행한 뒤 지정한 파일을 읽어 적절한 상황에 실행
#모듈이 개발자가 작성한 코드를 실행하는 형태의 모듈

#함수 데코레이터
#'@'로 시작하는 구문
#함수 데코레이터: 대상 함수의 앞뒤에 꾸밀 부가적인 내용을 데코레이터로 정의하여 손쉽게 사용
def test(function):
    def wrapper():
        print("인사가 시작되었습니다")
        function()
        print("인사가 종료되었습니다")
    return wrapper
@test
def hello():
    print("hello")
hello()
#최종적으로 hello에 함수가 들어가 hello() 형태로 호출
# 왜냐하면 test()함수에서 wrapper()함수를 리턴하기 때문

#모듈만드는 법 - module_basic 디렉토리에!

