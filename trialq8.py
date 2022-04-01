#class
#object oriented programming language = create object based on class

#Objects
#우리가 어떤 데이터를 활용하는가?
#abstraction - describing an object using relevant elements, not all elements
#taking key concepts and functions from complex data, modules, or systems

students = [{"name": "a", "korean":87, "math":98, "english":88, "science":95},
            {"name": "b", "korean":92, "math":70, "english":58, "science":96},
            {"name": "c", "korean":46, "math":95, "english":86, "science":95},
            {"name": "d", "korean":97, "math":96, "english":90, "science":93},
            {"name": "e", "korean":83, "math":69, "english":94, "science":95}
            ]
print("이름", "총점", "평균", sep="\t")
for student in students:
    score_sum = student["korean"] + student["math"] + student["english"] + student["science"]
    score_average = score_sum/4
    print(student["name"], score_sum, score_average, sep="\t")

#student in the form of dictionary combined in a list
#object refers to anything that can include elements
##e.g. student, and students

#make a function that creates a dictionary
def create_student(name, korean, math, english, science):
    return{"name":name, "korean":korean, "math":math, "english":english, "science":science}

students = [create_student("a", 87, 98, 88, 85),
            create_student("b", 92, 70, 58, 96),
            create_student("c", 46, 95, 86, 95),
            create_student("d", 83, 69, 94, 95)
            ]

print("이름", "총점", "평균", sep="\t")
for student in students:
    score_sum=student["korean"]+student["math"]+student["english"]+student["science"]
    score_average=score_sum/4
    print(student["name"], score_sum, score_average, sep="\t")

#학생을 매개변수로 받는 형태로 함수를 만든다면?
#학생 객체와 관련된 부분:##
##딕셔너리 리턴
##학생 처리 함수 (총점 구하기, 평균 구하기, 출력될 형태 만들기)
# 이 객체를 활용하는 처리 구분: ##
##학생 리스트 선언
##학생 한 명씩 반복 + 출력

def create_student(name, korean, math, english, science):
    return {"name":name, "korean":korean, "math":math, "english":english, "science":science}
def student_get_sum(student):
    return student["korean"] + student["math"] + student["english"] + student["science"]
def student_get_average(student):
    return student_get_sum(student) /4
def student_to_string(student):
    return "{}\t{}\t{}".format(student["name"], student_get_sum(student), student_get_average(student))

students = [create_student("a", 87, 98, 88, 85),
            create_student("b", 92, 70, 58, 96),
            create_student("c", 46, 95, 86, 95),
            create_student("d", 83, 69, 94, 95)
            ]
print("이름", "총점", "평균", sep="\t")
for student in students:
    print(student_to_string(student))
#이렇게 만들면 '학생 객체외 관련된 기능'을 별도의 모듈로 빼어 관리할 수도 있다
#객체와 관련된 코드를 분리할 수 있게 하는 것이 객체 지향 프로그래밍이다
#class: 위 형태의 코드를 더 효율적으로 만드는 기능

##Class 선언
#class class_name:
#   class_content
#인스턴스 이름(변수 이름) = 클래스 이름()
class Student:
    pass
student = Student()
students = [
    Student(),
    Student(),
    Student(),
    Student(),
    Student(),
    Student()
    ]

#생성자 (constructor)
#클래스 내부에 __int__ 라는 함수를 만들면 객체를 생성할 때 처리할 내용을 작성할 수 있다
#class class_name:
#   def __init__(self, 추가적 매개변수):
#       pass
#클래스 내부의 함수 첫 버내 매개변수로 반드시 self 입력할 것
#self는 자기 자신을 나타내는 딕셔너리임

class Student:
    def __init__(self, name, korean, math, english, science):
        self.name=name
        self.korean=korean
        self.math=math
        self.english=english
        self.science=science

students = [Student("a", 87, 98, 88, 85),
            Student("b", 92, 70, 58, 96),
            Student("c", 46, 95, 86, 95),
            Student("d", 83, 69, 94, 95)
            ]
students[0].name
students[0].korean

#소멸자 (destructor)
class Test:
    def __init__(self, name):
        self.name=name
        print("{} - 생성되었습니다".format(self.name))
    def __del__(self):
        print("{} - 소멸되었습니다".format(self.name))
test = Test("A")

#메소드 - 클래스가 가지고 있는 함수
class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
    def get_sum(self):
        return self.korean + self.math + self.english + self.science

    def get_average(self):
        return self.get_sum()/4
    def to_string(self):
        return "{}\t{}\t{}".format(self.name, self.get_sum(), self.get_average())

students = [Student("a", 87, 98, 88, 85),
            Student("b", 92, 70, 58, 96),
            Student("c", 46, 95, 86, 95),
            Student("d", 83, 69, 94, 95)
            ]
print ("이름", "총점", "평균", sep="\t")
for student in students:
    print(student.to_string())

#상속: 어떤 클래스를 기반으로 그 속성과 기능을 물려받아 새로운 클래스를 만듦
#isinstance(): 객체가 어떤 클래스를 기반으로 만들어졌는지 확인
#str(): 클래스의 특정 함수 호출

#isinstance()
#isinstance(인스턴스, 클래스)
#인스턴스가 해당 클래스를 기반으로 만들어졌다면 True, 아니면 False 리턴

class Student:
    def __init__(self):
        pass
student = Student()
print(isinstance(student, Student))
type(student)==Student
##type은 여기서는 같은 역할을 하지만 상속 관계를 확인하지는 않는다 - 예시:
class Human:
    def __init__(self):
        pass
class Student(Human):
    def __init__(self):
        pass
student=Student
print(isinstance(student, Human))
print(type(student)==Human)

#classroom이라는 리스트 안에 Student와 Teacher라는 클래스 생성
#요소가 Student 클래스의 인스턴스인지 Teacher 클래스의 인스턴스인지 확인
#각각 대상이 가지고 있는 적절한 함수 호출

class Student:
    def study(self):
        print("공부를 합니다")
class Teacher:
    def teach(self):
        print("학생을 가르칩니다")
classroom = [Student(), Student(), Teacher(), Student(), Student()]
for person in classroom:
    if isinstance(person, Student):
        person.study()
    elif isinstance(person, Teacher):
        person.teach()

#특수한 이름의 메소드
#특정한 상황에서 자동으로 호출된다
class Student:
    def __init__(self, name, korean, math, english, science):
        self.name=name
        self.korean=korean
        self.math=math
        self.english=english
        self.science=science
    def get_sum(self):
        return self.korean + self.math + self.english+self.science
    def get_average(self):
        return self.get_sum()/4
    def __str__(self):
        return "{}\t{}\t{}".format(
            self.name, self.get_sum(), self.get_average())

students = [Student("a", 87, 98, 88, 85),
            Student("b", 92, 70, 58, 96),
            Student("c", 46, 95, 86, 95),
            Student("d", 83, 69, 94, 95)
            ]
print("이름", "총점", "평균", sep='\t')
for student in students:
    print(str(student))
#str()함수의 매개변수를 넣으면 student의 __str__()함수가 자동으로 호출된다

#eq = equal
#ne = not equal
#gt = greater than
#ge = greater than or equal
#lt = less than
#le = less than or equal

class Student:
    def __init__(self, name, korean, math, english, science):
        self.name=name
        self.korean=korean
        self.math=math
        self.english=english
        self.science=science
    def get_sum(self):
        return self.korean+self.math+self.english+self.science
    def get_average(self):
        return self.get_sum()/4
    def __str__(self):
        return "{}\t{}\t{}".format(self.name, self.get_sum(), self.get_average())
    def __eq__(self, value):
        return self.get_sum() == value.get_sum()
    def __ne__(self, value):
        return self.get_sum() != value.get_sum()
    def __gt__(self, value):
        return self.get_sum() > value.get_sum()
    def __ge__(self, value):
        return self.get_sum() >= value.get_sum()
    def __lt__(self, value):
        return self.get_sum() < value.get_sum()
    def __le__(self, value):
        return self.get_sum() <= value.get_sum()

students = [Student("a", 87, 98, 88, 85),
            Student("b", 92, 70, 58, 96),
            Student("c", 46, 95, 86, 95),
            Student("d", 83, 69, 94, 95)
            ]
student_a=Student("a", 87, 98, 88, 85)
student_b=Student("b", 92, 70, 58, 96)

print(student_a == student_b)
print(student_a != student_b)

print(str(Student("a", 55, 55, 55, 55)))
