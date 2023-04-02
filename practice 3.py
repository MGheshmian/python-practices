n = (input("Enter a number:"))
t = list(n)
print("saal:", end="" + t[0] + t[1] + "\n")
print("mah:", end="" + t[2] + t[3])
# ****************************************
n = int(input('Enter the height:'))
for i in range(1, n+2):
    y = (2 * i) - 1
    print(" "*(n+1-i) + "*"*y)

for i in range(n, 0, -1):
    for j in range(n - i+1):
        print(' ', end='')

    for j in range(2 * i - 1):
        print('*', end='')
    print()
# *****************************************
n = int(input())
t = []
for i in range(n):
    j = input()
    t.append(j.title())
for i in t:
    print(i)
# *****************************************
a = input()
b = input()
c = input()
t = 0
x = len(b)
for i in range(x):
    if b[i] != c[i]:
        t += 1

print(t)
# *****************************************
y = []
n = True
while n:
    a = int(input("Enter a number:"))
    if a == 0:
        n = False
    else:
        y.append(a)

for i in y[::-1]:
    print(i, end="\n")
