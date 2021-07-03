# class Student:
    
#     def __init__(self, name, age, phoneNum, major):
#         self.name = name
#         self.age = age
#         self.phoneNum = phoneNum
#         self.major = major

#     def classes():
#         pass

#     def __str__(self):
#         return "이름: {}, 나이: {}세, 전화번호: {}, 학과: {}".format(self.name, self.age, self.phoneNum, self.major)

# ------------ 재귀 함수 예제.-----------------

# from os import close


# def factor(n):
#     if n == 1:
#         return 1
#     else:
#         return n*factor(n-1)

# result = factor(5)
# print(result)

# 1~n까지 더하기
# def plus(n):
#     total = 0
#     for i in range(n+1):
#         total += i
#     return total

# print(plus(10))

# 재귀함수로 만들기 (1부터 n까지 더하기)
# def plus(n):
#     if n==1:
#         return 1
#     else:
#         return n+plus(n-1)

# print(plus(10))
# print(plus(100))

# ----------- 파일 -----------------
# f = open("menu.txt", "w")
# f.write("Hello Python Programming")
# f.close()

# f = open("menu.txt", "a")
# f.write("I'm learning python language. I enjoy learning python language")
# f.close()

# f = open("d:/menu.txt", "w")
# f.write("아메리카노 : 3,000\n")
# f.write("카페 라떼 : 3,200\n")
# f.write("카페 모카 : 3,500\n")
# f.write("아이스티 : 3,500")
# f.close()

# f = open("d:/menu1.txt", "r")
# line=f.read()
# print(line)
# f.close()


# --------------------- Exception ---------------------


try:
    file=open("d:/menu.txt", "r")
    f = file.read()
    print(f)
except Exception as e:
    print(e)
    # if file is not None:
    #     file.close()
else:
    print("No error")
    file.close()
finally:
    print("프로그램 종료")
    
