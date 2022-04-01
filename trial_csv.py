#처리할 데이터 양이 많아지면 csv 형식 데이터를 사용한다
#csv - 쉼표로 나눠진 값
#텍스트 에디터로 csv 만들어도 엑셀에서 열면 쉽표를 기준으로 데이터를 잘 나누게 된다
#파이썬에서는 csv 모듈 사용 (csv형 리스트=[list_A], [list_B],...)
#read: csv파일을 파이썬 가공 파일로 불러오는 것
#write: 파이썬 가공 파일을 csv파일로 저장하는 것

import csv, os
os.chdir(r"/home/neurlab-dl3/anaconda3/envs/dfdf/bin")
f = open('a.csv', 'r')
new=csv.reader(f)
for i in new:
    print(i)
#csv형 리스트로 바꾸기
f.seek(0)
a_list=[]
for i in new:
    a_list.append(i)
print(a_list)
#함수로 만들기
def opencsv(filename):
    f=open(filename, 'r')
    reader=csv.reader(f)
    output=[]
    for i in reader:
        output.append(i)
    return output
    f.close()
print(opencsv("example2.csv"))

the_list=[['구', '전체', '내국인', '외국인'],
   ['관악구', '519864', '502089', '17775'],
   ['강남구', '547602', '542498', '5104'],
   ['송파구', '686181', '679247', '6938']]
def writecsv(filename, the_list):
    with open(filename, 'w', newline='') as f:
        a=csv.writer(f, delimiter=',')
        a.writerows(the_list)
writecsv("file_trial.csv", the_list)
file=opencsv("file_trial.csv")
import re
i=file[2]
k=[]
for j in i:
    if re.search('\d', j):
        k.append(float(re.sub(',', '', j)))
    else:
        k.append(j)
print(k)
#or
k=[]
for j in i:
    if re.search('[a-z가-힣]', j):
        k.append(j)
    else:
        k.append(float(re.sub(',', '', j)))
print(k)
#or
h=file[2]
print(h)
for j in h:
    if re.search('[a-z가-힣!]', j):
        i[i.index(j)]=j
    else:
        i[i.index(j)]=(float(re.sub(',', '', j)))
print(h)
#or
h=file[2]
for j in h:
    try:
        i[i.index(j)]=(float(re.sub(',', '', j)))
    except:
        pass
print(h)

def switch(listName):
    for i in listName:
        for j in i:
            try:
                i[i.index(j)]=(float(re.sub(',', '', j)))
            except:
                pass
    return listName
##외국인 비율이 3%가 넘는 구 정보만 csv 파일로 저장
list_foreigners=[['합계', '한국인', '등록외국인', '고령자'],
                 ['합계', '9,740,398', '285,529', '1,468,146'],
                 ['종로구', '151,767', '11,093', '27,394'],
                 ['송파구', '677,489', '6,849', '86,062'],
                 ['강동구', '426,219', '4,303', '61,710']]
writecsv("file_trial2.csv", list_foreigners)
total=opencsv("file_trial2.csv")
newPop=switch(total)
print(newPop)

for i in newPop:
    foreign = 0
    try:
        foreign=round(i[2]/(i[1]+i[2])*100, 1)
        print(i[0], foreign)
    except:
        pass

new=[["구", "한국인", "외국인", "외국인 비율"]]
for i in newPop:
    foreign=0
    try:
        foreign=round(i[2]/(i[1]+i[2])*100, 1)
        if foreign > 3:
            new.append([i[0], i[1], i[2], foreign])
    except:
        pass

writecsv('newPop.csv', new)
print(opencsv('newPop.csv'))
#자료 가공 (using writecsv, opencsv, switch)
#일부만 출력해보기
#csv파일로 저장= 빈 리스트 만들고, if 조건에 취합하면, 리스트에 append!

##csv 파일에 문장들 정리하기 (예: 한쪽에는 원본, 한쪽에는 번역본)
import re, os
English = "Once when I was six years old I saw a magnificent picture in a book, called TrueStories from Nature, about the primeval forest. It was a picture of a boa constrictorin the act of swallowing an animal. Here is a copy of the drawing."
Korean = "내가 여섯 살이었을 때 나는 원시림에 관한 TrueStories from Nature라는 책에서 웅장한 그림을 보았다. 동물을 삼키는 행위를하는 보아 뱀의 사진이었다. 다음은 그림의 사본입니다."
English_list=re.split('\.', English)
Korean_list=re.split('\.', Korean)
total=[]
for i in range(len(English_list)):
    total.append([English_list[i], Korean_list[i]])
writecsv('Korean_English.csv', total)
print(opencsv('Korean_English.csv'))
