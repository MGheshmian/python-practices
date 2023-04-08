import numpy as np
r = np.ones(5).reshape(1, 5)
a = np.concatenate([np.arange(0, 5).reshape(1, 5), np.array(np.arange(0, 5)[::-1]).reshape(1, 5)], axis=0)
d = np.arange(1, 20, 2).reshape(2, 5)
b = np.concatenate([r, a], axis=0)
c = np.concatenate([b, d], axis=0)
print(c)
