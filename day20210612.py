# a = [1, 2, 3, 4]
# print(a)


# for문
# for i in range(10):
#     print(i)


# for i in range(0, 13, 2):
#     print(i)

# for i in range(13, 0, -2):
#     print(i)

# for i in range(0, 101, 3):
#     print(i)

# 100까지의 합 구하기
# sum = 0

# for i in range(11):
#     sum += i
    
# print(sum)


# a = list(range(21))

# print(7 in a)

# b = ['hello', 'word', 4, 5, 6, 3, True]

# for i in b:
#     print(i)


# i = 0
# sum = 0

# while i < 10:
#     sum += i
#     i += 1

# print(sum)

# i = -1

# while i < 30:
#     i += 3
#     print(i)

# 구구단 출력
# for i in range(2,10):
#     for j in range(1,10):
#         print('{} x {} = {}'.format(i, j, i*j))
#     print()


i = 2

while i < 10:
    j = 1
    while j < 10:
        print('{} x {} = {}'.format(i, j, i*j))
        j += 1
    i += 1
    print()
    