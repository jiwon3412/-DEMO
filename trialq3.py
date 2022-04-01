#함수 - 매개변수 넣기
def print_n_times(value, n):
    for i in range(n):
        print(value)

print_n_times ("Hello", 5)

#가변 매개변수
def print_n_times(n, *values): #가변 매개변수 뒤에 일반 매개변수를 쓸 수 없기 때문에 n을 앞으로 밀었다
    for i in range(n):
        for value in values:
            print(value)
        print() #print되는 value들 사이에 공간을 띄워줌

print_n_times(3, "a", "b", "c")

#기본 매개변수 - 기본값 포함 형태 (기본 매개변수 뒤에는 일반 매개변수가 올 수없다)
def print_n_times(value, n=2):
    for i in range(n):
        print(value)
print_n_times("안녕하세요")

#가변 매개변수와 기본 매개변수를 동시에 사용하는 방법??
#매개변수 이름을 지정해서 입력해야 한다
# 가변 매개변수 안에는 value를 여러 개 입력할 수 있으므로 가변 매개변수를 앞에 두고 기본 매개변수들이 들어가 있는 형태
def print_n_times(*values, n=2):
    for i in range(n):
        for value in values:
            print(value)
        print()
print_n_times("a", "b", "c", n=3)

#return
def sum_all(start=0, end=100, step=1):
    output=0
    for i in range(start, end+1, step):
        output+=i
    return output
print(sum_all(0, 100, 10))

def mul(*values):
    output=1
    for value in values:
        output = output * value
    return(output)
print(mul(5, 7, 9, 10))

#재귀 함수 - 자기 자신을 호출하는 것
def factorial(n):
    output=1
    for i in range(1, n+1):
        output*=i
    return output
print(factorial(5))
print(1*2*3*4*5)
#factorial(n)= n * factorial(n-1) (if n>=1)
def factorial2(n):
    if n==0:
        return 1
    else:
        return n * factorial2(n-1)
print(factorial2(5))

#Fibonacci recursion
#1st = 1
#2nd = 2
#nst = (n-1)+(n-2)
def fibonacci(n):
    if n==1:
        return 1
    if n==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(5))
print(2+3)
#재귀함수를 할때 반복하는 연산 수
counter = 0
def fibonacci2(n):
    print("Working out fibonacci({})..".format(n))
    global counter #to refer to an external variable, which is 'counter'
    counter += 1
    if n==1:
        return 1
    if n==2:
        return 1
    else:
        return fibonacci2(n-1) + fibonacci2(n-2)

print(fibonacci2(10), " number of addition in calculation: {}".format(counter))

#메모화 - 출력이 훨씬 빠르다 (한번 계산한 값을 저장하기 때문에 처리를 수행하지 않아도 됨)
dictionary = {1: 1, 2:1}
def fibonacci3(n):
    if n in dictionary:
        return dictionary[n]
    else:
        output=fibonacci3(n-1) + fibonacci3(n-2)
        dictionary[n] = output
        return output
print(fibonacci3(10))
print(dictionary)

#가독성 높이기 - 예시: 숫자를 받아 원의 둘레와 넓이 출력
number_input_a = input("number: \n ")
radius = float(number_input_a)
print(2 * 3.14 * radius)
print(3.14 * radius * radius)

def number_input():
    output = input("number: \n ")
    return float(output)
def get_circumference(radius):
    return 2*3.14*radius
def get_circle_area(radius):
    return 3.14*radius*radius
radius = number_input()
print(get_circumference(radius))
print(get_circle_area(radius))

def p(content):
    return "<p>{}</p>".format(content)
print(p("Hello!"))


def flatten(data):
    output=[]
    for i in data:
        if type(i) == int:
            output.append(i)
        else: output.extend(flatten(i))

    return output


example = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
print(example)
print(flatten(example))

#number of possible ways for 100 people to share tables.
#The maximum number of people per each table: 10
#The minimum number of people that per each table: 2

#def 함수(매개변수):
#   변수=초깃값
#   여러 가지 처리
#   return 변수
min_number_t = 2
max_number_t = 10
total_number = 100
memo = {}

def number_ways(left_number, occupying_number):
    key = str([left_number, occupying_number])
    if key in memo:
        return memo[key]
    if left_number < 0:
        return 0
    if left_number == 0:
        return 1
    count = 0
    for i in range(occupying_number, max_number_t + 1):
        count += number_ways(left_number-i, i)
    memo[key] = count

    return count

print(number_ways(total_number, min_number_t))
