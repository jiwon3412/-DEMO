#tuple: 자료형. 한번 결정된 요소는 바꿀 수 없음
#(data, data, data, data..)
tuple_test = (10, 20, 30)
tuple_test[0]
#tuple_test[0] = 1 #내부 요소 변경 불가
#요소 하나만 가지는 튜블 선언하려면 쉼표 추가 e.g. (273,)
#튜플 유용한 점 1: 괄호 x
[a, b] = [10, 20]
(c, d) = (10, 20)
print(a)
print(b)
print(c)
print(d)

tuple_test = 10, 20, 30, 40
print(tuple_test)
print(type(tuple_test))
a, b, c = 10, 20, 30
print(a)
print(b)
print(c)

#튜플 유용한 점 2: 변수값 교환
a, b = 10, 20
print(a)
print(b)
a, b = b, a
print(a)
print(b)

def test():
    return(10, 20)
a, b = test()
print(a)
print(b)

for i, value in enumerate([1, 2, 3, 4, 5, 6]):
    print("{}번째 element: {}".format(i, value))
a, b = 97, 40
print(divmod(a, b))
x, y = divmod(a, b)
print(x)
print(y)

#lambda: 함수를 간단히 선언
def call_10_times(func):
    for i in range(10):
        func()
def print_hello():
    print("Hello")
call_10_times(print_hello)

#map(func,list) - 리스트의 요소를 함수에 넣고 리턴된 값으로 새로운 리스트 구성
#filter(func,list) - 리스트의 요소를 함수에 넣고 리턴된 값이 True인 것으로 새로운 리스트 구성
def power(item):
    return item * item
def under_3(item):
    return item < 3
list_input_a = [1, 2, 3, 4, 5]
output_a = map(power, list_input_a)
print(output_a)
print(list(output_a))
output_b = filter(under_3, list_input_a)
print(output_b)
print(list(output_b))
#print(output_a) - you get 'map object' or 'filter object'
#print(list(output_a)) - you force it to be converted into a list
power = lambda x: x * x
under_3 = lambda x: x < 3
list_input_a = [1, 2, 3, 4, 5]
output_a = map(power, list_input_a)
print(output_a)
print(list(output_a))

output_b = filter(under_3, list_input_a)
print(output_b)
print(list(output_b))

#simpler way:
list_input_a = [1, 2, 3, 4, 5]
output_a = map(lambda x: x * x, list_input_a)
print(output_a)
print(list(output_a))

output_b = filter(lambda x: x<3, list_input_a)
print(output_b)
print(list(output_b))

#processing files
#file_object = open("file_path", "mode")
#mode: w(write mode - new), a(append mode - add), r(read mode)
#file_object.close()

file = open("basic.txt", "w")
file.write("Hello Python Programming..!")
file.close()
#with - automatically open and close the stream
with open("basic.txt", "w") as file:
    file.write("Hello Python Programming..!")
with open("basic.txt", "r") as file:
    contents=file.read()
print(contents)
#csv - one data each sentence. ',' used to separate the data in each sentence.
import random
hanguls = list("가나다라마바사아자차카타파하")
with open("info.txt", "w") as file:
    for i in range(1000):
        name = random.choice(hanguls) + random.choice(hanguls)
        weight = random.randrange(40, 100)
        height = random.randrange(140, 200)
        file.write("{}, {}, {}\n".format(name, weight, height))

with open("info.txt", "r") as file:
    for line in file:
        (name, weight, height) = line.strip().split(",")
        if (not name) or (not weight) or (not height):
            continue
        bmi = int(weight)/((int(height)/100) **2)
        result = ""
        if 25 <=bmi:
            result = "과체중"
        elif 18.5 <=bmi:
            result = "정상 체중"
        else:
            result = "저체중"
        print('\n'.join(["이름: {}, 몸무게: {}, 키: {}, BMI: {}, 결과: {}"]).format(name, weight, height, bmi, result))
        print()

with open("test.txt", "w") as file:
    file.writelines(["This is 6th line\n", "This is 7th line"])
with open("test.txt", "r") as file:
    content = file.read()
    print(content)

#Generator - 직접 이터레이터를 만들 때 사용
# 함수 내부에 yield keyword 사용 (함수 호출해도 함수 내부 코드 실행 x)
def test():
    print("함수가 호출되었습니다.")
    yield "test"

print("A 지점 통과")
test()

print("B 지점 통과")
print(test())
#제너레이터 객체를 리턴. next() 사용해야 함수 내부 코드 실행 가능
def test():
    print("A 지점 통과")
    yield 1
    print("B 지점 통과")
    yield 2
    print("C 지점 통과")
output = test()
print("D 지점 통과")
a = next(output)
print(a)
print("E 지점 통과")
b = next(output)
print(b)
print("F 지점 통과")
#c = next(output)
#print(c) #you get stopiteration

numbers = [1, 2, 3, 4, 5, 6]
print("::".join(map(lambda x: str(x), numbers)))

numbers = list(range(1, 10+1))
print(list(filter(lambda x: x%2==1, numbers)))
print(list(filter(lambda x: 3<=x<7, numbers)))
print(list(filter(lambda x: x*x<=50, numbers)))