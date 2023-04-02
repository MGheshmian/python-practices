# 1
n = int(input("Enter a number:"))
list = []
for i in range(1, n+1):
    i = (3*i + 2)/3
    list.append(i)


def f(list):
    c = 1
    for j in list:
        c = c * j
    return c

print(f(list))


# 3(sum of the digits of a number)
n = int(input("Enter a number:"))


def f(n):
    t = 0
    for i in str(n):
        t += int(i)
    return t


print(f(n))
