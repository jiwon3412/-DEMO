#예상치 못한 상황
#error
#syntax error - occurs before the program operates
#exception / runtime error - occurs while the program is operating

#Exception handling - 예외적 상황까지 생각하기!
#isdigit()
user_input_a = input("정수 입력> ")
if user_input_a.isdigit():
    number_input_a = int(user_input_a)
    print("반지름:", number_input_a)
    print("둘레:", number_input_a * 2 * 3.14)
    print("원 넓이:", number_input_a * number_input_a * 3.14)
else:
    print("정수를 입력하지 않았습니다.")

#try except
#try: 예외가 발생할 가능성이 있는 코드
#except: 예외가 발생했을 때 실행할 코드

try:
    number_input_a = int(input("정수 입력> "))
    print("반지름:", number_input_a)
    print("둘레:", number_input_a * 2 * 3.14)
    print("원 넓이:", number_input_a * number_input_a * 3.14)
except:
    print("무언가 잘못되었습니다.")

#pass: 예외이면 넘어가
list_input_a = ["52", "273", "32", "spy", "103"]
list_number = []
for item in list_input_a:
    try:
        float(item)
        list_number.append(item)
    except:
        pass
print("{} 내부에 있는 숫자는 {}입니다".format(list_input_a, list_number))
#else: 예외가 발생하지 않았을 때 실행할 코드
#반드시 except 뒤에 사용
try: number_input_a = int(input("정수입력>"))
except: print("정수를 입력하지 않았습니다")
else:
    print("반지름:", number_input_a)
    print("둘레:", number_input_a * 2 * 3.14)
    print("원 넓이:", number_input_a * number_input_a * 3.14)

#finally - 예외가 발생하든 발생하지 않든 무조건 실행
try:
    number_input_a = int(input("정수입력"))
    print("반지름:", number_input_a)
    print("둘레:", number_input_a * 2 * 3.14)
    print("원 넓이:", number_input_a * number_input_a * 3.14)
except:
    print ("정수 입력 부탁")
else:
    print("정상 작동")
finally:
    print("프로그램 종료")
#try + except
#try + except + else
#try + except + finally
#try + except + else + finally
#try + finally

#함수에서 try구문 쓸 때 중간에 return 해도 finally 구문 실행된다
def write_text_file(filename, text):
    try:
        file = open(filename, "w")
        return
        file.write(text)
    except Exception as e:
        print(e)
    finally:
        file.close()
write_text_file("text.txt", "안녕하세요")

with open("text.txt", "r") as file:
    content = file.read()
    print(content)

#index - 특정 값이 어디 있는지 확인
numbers = [1, 2, 3, 4, 5, 6]
numbers.index(2)

numbers = [52, 273, 32, 103, 90, 10, 275]
number = 10000
try: print("{} is at position {}".format(number, numbers.index(number)))
except: print("not in the list")

if number in numbers:
    print("{} is at position {}".format(number, numbers.index(number)))
else:
    print("not in the list")

#Exception object
#try: 예외가 발생할 가능성이 있는 구문
#else 예외의 종류 as 예외 객체를 활용할 변수 이름:
#   예외가 발생했을 때 실행할 구문
#모든 예외: Exception

try:
    number_input_a = int(input("integer"))
    print("반지름:", number_input_a)
    print("둘레:", number_input_a * 2 * 3.14)
    print("원 넓이:", number_input_a * number_input_a * 3.14)
except Exception as exception:
    print(type(exception), "\n", exception)

list_number = [52, 273, 32, 72, 100]
try:
    number_input = int(input("integer: "))
    print("{} at the position {}".format(list_number[number_input], number_input))
except ValueError:
    print("type an integer")
except IndexError:
    print("out of range")

try:
    number_input = int(input("integer: "))
    print("{} at the position {}".format(list_number[number_input], number_input))
except ValueError as exception:
    print("type an integer")
    print(exception)
except IndexError as exception:
    print("out of range")
    print(exception)
#모든 에러 잡기
except Exception as exception:
    print("unexpected error")
    print(type(exception), exception)

#구현되지 않은 부분에서 예외를 발생시켜 강제종료시키자
number=int(input("integer"))
if number> 0:
    raise NotImplementedError
else:
    raise NotImplementedError



