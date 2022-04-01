#클래스 변수

class Student:
    count = 0

    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

        Student.count += 1
        print("{}번째 학생이 생성됨".format(Student.count))

students = [Student("a", 87, 98, 88, 85),
            Student("b", 92, 70, 58, 96),
            Student("c", 46, 95, 86, 95),
            Student("d", 83, 69, 94, 95)
            ]

#print("현재 생성된 총 학생 수는 {}".format(Student.count))

#클래스 함수
#클래스가 가진 기능이라고 명시
#클래스 내에서 students라는 리스트 안에 학생 정보 넣어두기
#리스트 안의 학생을 한 명씩 반복하기
#학생 리스트를 선언하고 객체를 이용하는 것 다 클래스 안에서 하기 !!
class Student:
    count=0
    students=[]
    @classmethod
    def print(cls):
        print("-----학생 목록-----")
        print("이름\t총점\t평균")
        for student in cls.students:
            print(str(student))
        print("------------------")

    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        Student.count+=1
        Student.students.append(self)
    def get_sum(self):
        return self.korean+self.math+self.english+self.science
    def get_average(self):
        return self.get_sum()/4
    def __str__(self):
        return "{}\t{}\t{}".format(self.name, self.get_sum(), self.get_average())

Student("a", 87, 98, 88, 85),
Student("b", 92, 70, 58, 96),
Student("c", 46, 95, 86, 95),
Student("d", 83, 69, 94, 95)

Student.print()

###가비지 컬렉터: 더 이상 사용할 가능성이 없는 데이터를 메모리에서 제거하는 역할
#사용 가능성이 없는 데이터란? 변수에 저장되지 않거나 함수 등에서 나오며 변수를 사용할 수 없게 되는 경우

class Test:
    def __init__(self, name):
        self.name=name
        print("{} - 생성되었습니다".format(self.name))
    def __del__(self):
        print("{} - 파괴되었습니다".format(self.name))
Test("A")
Test("B")
#A가 생성되고 사용되지 않을 것이기 때문에 A를 제거하여 소멸 (A 생성, A 파괴, B 생성, B 파괴 반복)

class Test:
    def __init__(self, name):
        self.name = name
        print("{} - 생성".format(self.name))
    def __del__(self):
        print("{} - 파괴".format(self.name))
a = Test("A")
b = Test("B")
#이번에는 변수에 저장된다 - 사용가능성이 있으므로 프로그램 종료 전까지 메모리에서 제거하지 않는다

#프라이빗 변수와 게터/세터: 객체의 효율적 사용

import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def get_circumference(self):
        return 2 * math.pi * self.radius
    def get_area(self):
        return math.pi * (self.radius ** 2)
circle = Circle(10)

#만약 음수를 넣는다면 둘레가 음수로 나올 것이다. 길이를 음수로 넣는 것을 막아야 함.

#프라이빗 변수: 클래스 내부의 변수가 외부 사용되는 것을 막기 위해 __<변수이름> 선언
#게터와 세터 : 외부에서 간접적으로 __radius 속성 접근
# ###프라이빗 변수의 값을 추출하거나 변경할 목적으로 사용됨
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def get_circumference(self):
        return 2 * math.pi * self.radius
    def get_area(self):
        return math.pi * (self.radius ** 2)

    #게터 세터 선언
    def get_radius(self):
        return self.radius
    def set_radius(self, value):
        self.radius = value
circle = Circle(10)
#프라이빗 변수 썼기 때문에 print(circle.__radius) 불가능
print("둘레: ", circle.get_circumference())
print("넓이: ", circle.get_area())

print(circle.get_radius())
circle.set_radius(2)

#세터 사용하여 음수 하기
#def set_radius(self, value):
#    if value <==0:
#        raise TypeError("길이는 양의 숫자이어야 한다")
#    self.__radius = value

#데코레이터 사용하여 게터 세터 만들기
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def get_circumference(self):
        return 2 * math.pi * self.__radius
    def get_area(self):
        return math.pi * (self.__radius ** 2)
    @property
    def radius(self):
        return self.__radius
    @radius.setter
    def radius(self,value):
        if value<=0:
            raise TypeError("길이는 양의 숫자이어야 함")
        self.__radius = value

circle = Circle(10)
print(circle.radius)
circle.radius = 2
print(circle.radius)

#상속: 누군가 만들어 놓은 기본 형태에 내가 원하는 것만 교체하는 것
#다중 상속: 누군가 만들어 놓은 형태를 조립하여 내가 원하는 것을 만드는 것

class Parent:
    def __init__(self):
        self.value="테스트"
        print("Parent 클래스의 __init()__메소드가 호출되었습니다")
    def test(self):
        print("Parent 클래스의 test() 메소드입니다")
class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        print("Child 클래스의 __init()__ 메소드가 호출되었습니다")

child = Child()
child.test()
print(child.value)


