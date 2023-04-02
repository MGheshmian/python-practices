# 1
n = int(input('Enter the height:'))
for i in range(1, n+1):
    y = (2 * i) - 1
    print(" "*(n-i) + "*"*y)

# 2 (detecting if a number is prime)
n = int(input("Enter a number:"))
x = 0
for i in range(1, n+1):
    if n % i == 0:
        x += 1

if x == 2:
    print("the number is prime")
else:
    print("the number is not prime")

# 3 ( prime numbers under 1000)
for i in range(2, 1000):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)
