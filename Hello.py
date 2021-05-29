# print("Hello coding python")

# x = 3
# y = 5
# print(x)
# print(y)
# print(x + y)
# print("x")

# print(x * y)
# print(x ** y)
# print(x % y)
# print(x - y)

# print(3.14)

# x = "Hello World"
# print(x)
# print("Hello World")

# print(10 // 3)
# print(10 % 3)
# print(10 / 3)

# x = 2
# y = "World"
# print(str(x) + y)

# x = 3
# print(x * "Hello ")
# print("Hello " * x)

# print('x =', x)


# 과제 (변수1에 13을 넣고, 변수2에 25를 넣은 후 두개의 합, 두개의 곱, 두개의 나머지 출력)

# n1 = 13
# n2 = 25

# print('n1 = 13, n2 = 25, sum =', n1+n2)
# print('n1 = 13, n2 = 25, multi =', n1*n2)
# print('n1 = 13, n2 = 25, rem =', n1%n2)
# print('n1 = 13, n2 = 25, rem =', n1%n2, ', multi =', n1*n2, ', rem =', n1%n2)

# 원의 둘레와 넓이 구하기
# pi = 3.14159265
# r = 5

# print("원주율 =", pi)
# print("반지름 =", r)
# print("원의 둘레 =", 2*pi*r)
# print("원의 넓이 =", pi*r*r)



# i = 100
# i //= 5
# i -= 12
# i += 3
# print(i)


# input
# name = input('이름을 입력해주세요 : ')
# age = input('나이를 입력해주세요 : ')
# print(name)
# print(age)


# 형변환
# n = 14
# n = str(n)
# print(n)

# format 사용
# x = 13
# y = 55

# print('x = {}' .format(x))
# print('y = {}' .format(y))
# print('{} + {} = {}' .format(x, y, x+y))


# 출력 길이 다루기 
x = 77 # 정수
print('x = {:5d}' .format(x)) # decimal 5칸을 차지해라
print('x = {:05d}' .format(x))

str = 'x = {:05d}' .format(x)
print(str)

y = 3.2457 # 실수
print('y = {:.2f}' .format(y)) 
print('y = {:5.2f}' .format(y)) # :5 소수점을 포함한 전체 길이 
