w = float(input("Weight:"))
h = float(input("Height:"))
a = w / (h*h)
b = f'{a:.2f}'
print(b)
if float(b) < 18.5:
    print("Underweight")
elif 18.5 <= float(b) < 25:
    print("Normal")
elif 25 <= float(b) < 30:
    print("Overweight")
elif 30 <= float(b):
    print("Obese")
# **********************************
a = int(input("Enter a number:"))
b = int(input("Enter a number:"))
if a > b:
    print(a, "<", b)
elif b > a:
    print(b, "<", a)
else:
    print(a, "=", b)
# **********************************
n = input("Enter a number:")
t = 0

while len(n) != 1:
    for i in n:
        t += int(i)
    n = list(str(t))
    t = 0
print(''.join(n))
# **********************************
n = int(input())
y = int(input())
x = int(input())
for i in range(1, 100001):
    if i * y == n:
        print(i, 0)
        break
    elif i * x == n:
        print(0, i)
        break
    for j in range(1, 100001):
        if y*i + x*j == n:
            print(y, x)
        else:
            break
else:
    print(-1)
# **********************************
a = int(input())
b = int(input())
c = int(input())
if a > 0 and b > 0 and c > 0:
    if a + b + c == 180:
        print("Yes")
    else:
        print("No")
else:
    print("No")
