import os, re
os.getcwd()
os.chdir(r'/home/neurlab-dl3/anaconda3/envs/dfdf/bin')
f = open('friends101.txt', 'r')
script101=f.read()
print(script101[:100])
#모니카 대사만 모으기
Line=re.findall(r"Monica:.+", script101)
print(Line[:3])
for item in Line[:3]:
    print(item)
f.close()
f=open('monica.txt', 'w', encoding='utf8')
monica=''
for i in Line:
    monica += i +'\n'
f.write(monica)
f.close()
with open('monica.txt', 'r') as f:
    print(f.read()[:100])

#등장인물 리스트
#등장인물 (e.g. 'Monica:'): 대문자 시작, 소문자 반복, 콜론
char=re.compile(r'[A-Z][a-z]+:')
print(re.findall(char,script101))
#중복값 지우기
print(set(re.findall(char,script101)))
#콜론 지우기
y=set(re.findall(char,script101)) #리스트를 집합으로 바꾼다
z=list(y)#집합을 리스트로 다시 바꿔
character=[]
for i in z:
    character +=[i[:-1]]
#한마디로
character=[x[:-1] for x in list(set(re.findall(r'[A-Z][a-z]+:', script101)))]
print(character)

#지문만 출력
#괄호+문자(대문자/소문자) 시작 + 공백 진행 + 소문자/마침표 +닫는 괄호
#.+ - 문자 숫자 등 자유롭게 반복
#영어 소문자 또는 마침표 [a-z|\.]
print(re.findall(r'\([A-Za-z].+[a-z|\.]\)', script101)[:6])

#특정 단어의 예문 모으기
#문장을 원소로 하는 리스트
f=open('friends101.txt', 'r')
sentences=f.readlines()
for i in sentences[:20]:
    if re.match(r'[A-Z][a-z]+:', i):
        print(i)
lines=[i for i in sentences if re.match(r'[A-Z][a-z]+:', i)]
lines[:10]
would=[i for i in sentences if re.match(r'[A-Z][a-z]+:', i) and re.search('would', i)]
print(would)