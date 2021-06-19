# a = { 'name':'Eunbi', 'age':29, 'region':'Cheonan'}

# for x in a:
#     print(x)


# for x in a.values():
#     print(x)


# class1 = [{'name':'John', 'eng':80, 'mat':90}]
# print(class1)

# class1[0]['science']=100
# print(class1)





# 빈문자열이 들어올때까지, 학생의 이름을 읽어들여서 리스트 안의 딕셔너리에 저장하는 프로그램
# student = []

# sname = input("이름 : ")

# while(sname != ""):
#     student.append({'name':sname})
#     sname = input("이름 : ")

# print(student)




# 각 학생의 이름, 영어점수, 수학점수를 입력받고 학생정보는 딕셔너리에, 모든 학생은 리스트에 저장
# students = []
# sname = input("이름 : ")
# esum = 0
# msum = 0
# eavg = 0
# mavg = 0

# while sname != '':
#     mat = int(input("수학점수 : "))
#     eng = int(input("영어점수 : "))
#     student = {"이름":sname, "수학점수":mat, "영어점수":eng}
#     students.append(student)
#     sname = input("이름 : ")

# for student in students:
#     print(mat)
#     msum += student["수학점수"]
#     esum += student["영어점수"]

# mavg = msum / len(students)
# eavg = esum / len(students)

# print('수학점수의 총합 : {}'.format(msum))
# print('영어점수의 총합 : {}'.format(esum))

# print('수학점수 평균 : {:.1f}'.format(mavg))
# print('영어점수 평균 : {:.1f}'.format(eavg))


# 위의 문제를 함수를 사용
# def getPoint(name):
#     eng = int(input("영어점수 : "))
#     mat = int(input("수학점수 : "))
#     student = {"name":name, "eng":eng, "mat":mat}
#     return student

# students = []
# while True:
#     name = input("이름 : ")
#     if name == '':
#         break;
#     students.append(getPoint(name))

# print(students)

# 소수 구하기
# nums = [n for n in range(100) if ]