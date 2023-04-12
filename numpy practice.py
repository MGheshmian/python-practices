# 1
import numpy as np
r = np.ones(5).reshape(1, 5)
a = np.concatenate([np.arange(0, 5).reshape(1, 5), np.array(np.arange(0, 5)[::-1]).reshape(1, 5)], axis=0)
d = np.arange(1, 20, 2).reshape(2, 5)
b = np.concatenate([r, a], axis=0)
c = np.concatenate([b, d], axis=0)
print(c)
# 2
print(np.zeros(10))
# 3
a = np.zeros(10)
a[4] = 1
print(a)
# 4
print(np.arange(10, 50))
# 5
print(np.arange(5)[::-1])
# 6
print(np.arange(0, 9).reshape(3, 3))
# 7
print(np.eye(3))
# 8
a = (np.array(np.eye(3)))
print(a.astype(int))
# 9
a = np.random.randint(1, 101, 9)
print(a.reshape(3, 3))
# 10
a = np.random.randint(0, 6, 10)
b = list(a)
print(a)
for i in b:
    if i != 0:
        print(b.index(i))
# 11
x = np.array([[10, 20, 4],
             [23, 56, 70]])
e = x.size
d = x.itemsize
print("Memory size in bytes:", e*d)
