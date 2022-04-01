#if 조건문
number = int(input("type any number:\n "))
if number>0:
    print("It is a positive number")
if number<0:
    print("It is a negative number")
if number==0:
    print("It is zero")

#날짜 시간
import datetime
now = datetime.datetime.now()
print("{}년 {}월 {}일 {}시 {}분 {}초".format(now.year, now.month, now.day, now.hour, now.minute, now.second))
if now.hour < 12:
    print("오전 {}시".format(now.hour))
if now.hour>=12:
    print("오후 {}시".format(now.hour))

import datetime
now = datetime.datetime.now()
month = now.month
if 3 <= month <=5:
    print("It is spring now")
elif 6<= month <= 8:
    print("It is summer now")
elif 9<= month <=11:
    print("It is autumn now")
else: #month==12 or 1<= month <=2
    print("It is winter now")

#홀수 짝수
number = input("type any number:\n")
last_character = number[-1]
last_number = int(last_character)
if last_number % 2 == 0 : #if last_character in "02468":
    print("It is an even number")
else: #if last_number % 2 == 1:
    print("It is an odd number")

#elif 쓸 때 상위 값 생략 가능 - 이미 위에서 검사하였기 때문
#None, 0, 빈 컨테이너는 false 값으로 변환됨
#if: else: 뒤에 pass keyword 넣어주면 "곧 개발하겠음"이라는 의미 & raise NotImplementedError

#list [element, element, element], 여러 종류 자료형 포함 가능
list_a = [1, 2, 6, "camel", True] #[0, 1, 2, 3, 4] [-5, -4, -3, -2, -1]
list_b = [2, 3, 4]
print(list_a)
print(list_a[0])
print(list_a[1:3]) #[1] 과 [2] 출력함 ([3]을 기준으로 왼쪽 제거)
list_a[4]=False
print(list_a[3][2])
print(list_a+list_b)
print(len(list_a))
list_b.append(5) #맨 뒤에 요소 추가
list_a.insert(2, 3) #중간에 요소 추가 e.g. [2]에 숫자 3 넣기
list_b.extend([6, 7, 8]) #한번에 여러 요소 뒤에 추가
print(list_b)
print(list_a)
del list_a[4] #인덱스로 요소 제거
list_a.pop(3) #다른 방법으로 요소 제거
print(list_a)
list_b.remove(2) #값으로 요소 제거 (2를 지워달라) - 만약에 두개 있으면 가작 앞쪽에 하나만 제거됨
list_a.clear() #모든 요소 제거

#for - 반복문
for i in range(100): #100번 print 출력
    print("print")

list_c = [2, 66, 257, 1, 43674, 2]
for element in list_c:
    if len(str(element))==1:
        print(str(element), " 는 1 자릿수입니다")
    elif len(str(element))==2:
        print(str(element), " 는 2 자릿수입니다")
    elif len(str(element))==3:
        print(str(element), " 는 3 자릿수입니다")
    elif len(str(element))==4:
        print(str(element), " 는 4 자릿수입니다")
    elif len(str(element))==5:
        print(str(element), " 는 5 자릿수입니다")

list_c = [2, 66, 257, 1, 43674, 2]
for element in list_c:
    print(str(element), " 는 {} 자릿수입니다".format(len(str(element))))

#Dictionary: 키를 기반으로 값을 저장한다 (리스트는 인덱스를 기반으로 저장)
dict_b = {"name":["A", "B", "C"], "gender":["male", "female", "female"], "age":[15, 48, 63]}
print(dict_b["age"][1])
dict_b["name"][2] = "CC"
print(dict_b)
dict_b["nationality"]=["USA", "China", "Canada"]
del dict_b["nationality"]
dict_b.get("Occupation") #print none rather than generating KeyError
for key in dict_b:
    print(dict_b[key])

#Range
list(range(10))
a=list(range(0, 5, 2)) #0부터 4까지 두 칸 띔
print(a)
a=list(range(0, 10+1, 1)) #0부터 10까지 (10 포함 강조)
print(a)
a=list(range(5, 0-1, -1)) #5부터 0까지 거꾸로 (0 포함 강조)
print(a)
array=[5, 2, 8, 4, 7]
for i in range(len(array)):
    print("{}번째 반복:{}".format(i, array[i]))
for i in reversed(range(5)):
    print(i)

#while
i=0
while i<10:
    print(i)
    i+=1

list_test=[1, 2, 2, 4, 6]
value=2
while value in list_test:
    list_test.remove(value)
print(list_test)

import time
number = 0
target_tick = time.time() + 3
while time.time()< target_tick:
    number+=1
print(number)

i=0
while True:
    print("{}st".format(i))
    i+=1
    input_text=input("quit(y/n):")
    if input_text in ["Y", "y"]:
        print("stop repetition")
        break

#continue - 다음 반복으로 pass
numbers = [1, 2, 6, 8, 3]
for number in numbers:
    if number>4:
        continue
    print(number)

limit = 100
i = 1
sum_value=0
while sum_value <= limit:
   sum_value += i
   i+=1
print("{}를 더할 때 {}를 넘으며, 그때의 값은 {}입니다.".format(i-1, limit, sum_value))

max_value=0
a=0
b=0
for i in range(1, 100):
    j=100-i
    current = i * j
    if max_value > current:
        a=i-1
        b=j+1
        break
    i += 1
    max_value = current
print("최대가 되는 경우:{} * {} = {}".format(a, b, max_value))

#reversed - generator 함수의 결과를 여러 번 활용하지 않고 함수를 넣음
numbers = [1, 2, 3, 4, 5]
for i in reversed(numbers):
    print(i)
print(list(reversed(numbers)))
print(numbers[::1])

#리스트의 요소를 반복할 때 인덱스 확인 - enumerate()
#does this:
list_d=["element 1", "element 2", "element 3"]
i=0
for item in list_d:
    print("{}st element: {}".format(i, item))
    i+=1

#for i in range(len(list_d)):
#    print("{}st element: {}.format(i, list_d(i)))
print(list(enumerate(list_d)))
for i, value in enumerate(list_d):
    print("{}st element: {}".format(i, value))

#items()
dict_c = {"A": "element 1", "B":"element 2", "C":"element 3",}
print(dict_c.items())

for key, element in dict_c.items():
    print("dictionary[{}] = {}".format(key, element))

array = []
for i in range(0, 20, 2):
    array.append(i * i)
#same as:
array = [i * i for i in range(0, 20, 2)]
print(array)

array = ["apple", "banana", "chocolate", "grapes"]
fruits = [fruit for fruit in array if fruit != "chocolate"]
print(fruits)

#join()
print("::".join(["1", "2", "3", "4"]))
number = int(input("정수 입력:\n"))
if number % 2 ==0:
    print("\n".join(["입력한 문자열은 {}입니다.",
                     "{}는 짝수입니다."
                     ]).format(number, number))
else:
    print("\n".join(["입력한 문자열은 {}입니다.",
                     "{}는 홀수입니다."
                     ]).format(number, number))

#iterate 가능한 것 = next() 함수를 적용하여 꺼낼 수 있는 요소
numbers = (1, 2, 3, 4, 5, 6)
r_num = reversed(numbers)
print(r_num)
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))

#python 진수 변환
b=format(10, "b")
print(b)
print("{:b}".format(10))#10진수 숫자를 2진수로 변환
print(int("1010", 2)) #2진수(따옴표 안에 있는 숫자)에서 10진수 변환

print("{:o}".format(10))
print(int("12", 8))

print("{:x}".format(10))
print(int("10", 16))
#2진수로 변화하였을 때 0이 하나만 포함된 숫자와 그의 합
output = [i for i in range (1, 100+1) if "{:b}".format(i).count("0")==0]
for i in range(1, 100+1):
   print("{} : {}".format(i, "{:b}".format(i)))
print("sum: ", sum(output))







