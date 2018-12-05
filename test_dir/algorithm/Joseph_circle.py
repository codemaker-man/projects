#  约瑟夫环
# 有m个人,围成一个环，编号为 1、2、3、、、m-1，从第一个人开始循环报数，假设数到n的那个人出列，
# 然后从下一个人继续数数，数到n出列，以此循环，最后那个人为胜利者，求胜利者的编号。

# 0 1 2 3  4:1  2:0

# def circle(m, n):  # 5 , 5
#     if n < 2:
#         raise ValueError('n must more than one!')
#     people = [i for i in range(0, m)] #
#     tmp = n
#     while len(people) > 1:
#         while tmp > len(people)-1:
#             tmp -= len(people)
#         people.pop(tmp)   #
#         tmp += n
#     return people
#
# print(circle(4,4))
# print(circle(4,2))

def josephus(n, k):
    if k == 1:
        raise ValueError('k must more than one!')
    p = 0
    people = list(range(1, n + 1))
    while True:
        if len(people) == 1:
            break
        p = (p + (k - 1)) % len(people)
        del people[p]
    print('survive:', people[0])


if __name__ == '__main__':
    josephus(10, 4)
    josephus(10, 2)
    josephus(10, 1)


