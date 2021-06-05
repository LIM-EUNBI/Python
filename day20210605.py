# # 대문자로 변환
# x = 'hello world'
# print(x.upper())
# x = x.upper()
# print(x)

# # 소문자로 변환
# print(x.lower())
# x = x.lower()
# print(x)

# # 공백 제거
# x = '    hello world    '
# print('{'+x+'}')
# print(x.strip())
# x = x.strip()
# print(x)

# # x라는 변수에 해당 문자를 포함하고 있는지 체크
# print("he" in x)
# print("c" in x)

# # 문자열 자르기 split (데이터를 자를 때 많이 사용)
# str = "10 20 30 40 50"
# ar = str.split() # 공백을 기준으로 자르기
# print(ar)

# str = "10.20.30.40.50"
# ar = str.split('.') # .을 기준으로 자르기
# print(ar)

# str = "10#20#30#40#50"
# ar = str.split('#') # #을 기준으로 자르기
# print(ar)


# 비교 연산
# a = 5
# b = 5

# print(a == b)
# print(a != b)
# print(a < b)
# print(a > b)
# print(a <= b)
# print(a >= b)

# a = 10
# b = 5

# print(a == b)
# print(a != b)
# print(a < b)
# print(a > b)
# print(a <= b)
# print(a >= b)

# a = "Hello"
# b = "World"
# print(a==b)
# print(a!=b)
# print(a>b)
# print(a<b)

# print('abyss' > 'abroad')

# if문
# x = 5;
# y = 5;

# if x==y:
#   print(True)
# else:
#   print(False)

# if문 활용1
# x = int(input("x의 값 : "))
# y = int(input("y의 값 : "))

# if x<y:
#     print(x)
# else:
#     print(y)

# if문 활용2
# a = int(input("a의 값 : "))
# b = int(input("b의 값 : "))

# if (b*4)==a:
#     print(a)
# else:
#     print(b)

# if문 활용3
# val = int(input("val의 값 : "))

# if val%3==0:
#     print("{}, 3의 배수".format(val))
# else:
#     print("{}, 3의 배수가 아님".format(val))

# if문 활용4
# num = int(input("값을 입력해주세요 : "))

# if num%3==0 and num%2==0:
#     print("{}, 3과 2의 공배수".format(num))
# else:
#     print(num) 

 # if~elif~else

x = int(input("x의 값 : "))

if x%3==0:
    print("{}(은)는, 3의 배수입니다.".format(x))
elif x%5==0:
    print("{}(은)는 5의 배수입니다.".format(x))
elif x%2==0:
    print("{}(은)는 2의 배수입니다.".format(x))
else:
    print("{} 해당 없음".format(x))