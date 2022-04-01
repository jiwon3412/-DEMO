#site:python-reference.readthedocs.io
#import only appears when you are using a valid function that requires what you are trying to import
import keyword
print(keyword.kwlist)
#줄바꿈
print()
#여러개 출력
print(1, 2, 3, 4, 5)
#연결하여 새로운 string
print("Oran"+"ge")
#1 2 3 4 5

#class
print(type("hello"))

#escape character
print("He said \"hello\"")
print("Hello\nHello")
#Hello
#Hello
print("Hello\tHello")
#Hello  Hello
print("""He said Hello 
He said Hello""")
#줄바꿈 using 'enter'

#Index - start from 0 (e.g. 0, 1, 2, 3, 4 for "Hello")
print("Hello"[0])
print("Hello"[1:4]) #ell
hello = "안녕하세요"
print(hello[:3])
#backward - (e.g. -1, -2, -3, -4, -5 for "Hello")
print("Hello"[-1])
#length - len
print(len("Hello"))

#int - 정수; float - 실수
#정수 나누기 //; 나머지 %; 제곱 **;
#a+=10 (a=a+10)

#input (always string)
name = input("What is your name:\n")
print(name)

number=int(input("Type any number:\n"))
print("The given number times 3 equals: ", number*3)

#Swap
A=30
B=50
A, B = B, A
print(A, B)

#anything to string using format function
string_number="{} {} {}".format(10, 20, 30)
print(string_number)
print(type(string_number))

format_a="I'm going home at {}".format(5)
print(format_a)

#printing integers using format function
output1 = "{:d}".format(52)
print(output1)
#5칸 밀기
output2 = "{:5d}".format(52)
print(output2)
#5칸 미는데 기호를 1)뒤로 2)앞으로
output3 = "{:+5d}".format(52)
print(output3)
output4 = "{:=+5d}".format(52)
print(output4)
#빈칸을 원하는 숫자로 채우기 (e.g. 5칸을 잡고 빈칸 0으로 채워)
output5 = "{:05d}".format(52)
print(output5)

#printing floats using format function
output1 = "{:f}".format(52.1)
print(output1)
#52.100000
#15칸에 부호 추가하고 0으로 채우기
output2 = "{:+015f}".format(52.1)
print(output2)
#0000052.100000
#소수점 3자리
output3 = "{:.3f}".format(52.1)
print(output3)
#52.100
#의미없는 소수점 제거
output4 = "{:g}".format(52.100)
print(output4)
#52.1

#Upper or lower (원본 유지되므로 비파괴적 함수)
a = "hello"
print(a.upper())

#strip():공백 제거 (탭, 줄바꿈, 띄어쓰기 포함)
#lstrip(): 왼쪽 공백 제거; rstrip(): 오른쪽 공백 제거
a = "   \n          Hello    "
print(a)
print(a.strip())

#is...(): 문자열 구성 파악
##e.g. isalpha(): 알파벳만?; isdecimal(): 정수형태?; islower(): 소문자만?
##출력: True or False
print("TrainA2".isalnum())

#find(): 왼쪽부터 문자 위치 찾아줌
#rfind(): 오른쪽부터 문자 위치 찾아줌
a = "안녕안녕하세요"
print(a.find("안녕"))
print(a.rfind("안녕"))

#in: 문자열에 이것을 포함하고 있는가
##출력: True or False
print("H" in "Hello")

#split():문자열을 특정한 문자로 자르자
##출력:list
print("비행기나소방차나거북선".split("나"))

