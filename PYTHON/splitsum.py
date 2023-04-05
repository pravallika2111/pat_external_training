# def splitsum(a):
#     l = []
#     c = 0
#     s = 0
#     for i in a:
#         if i > 0:
#             c += i**2
#         else:
#             s += i**3
#     l.append(c)
#     l.append(s)

#     return l


# l = [1, 3, -5]
# print(splitsum(l))

import pandas as pd
import os

data_csv = pd.read_csv("dumbb.txt", delimiter=" ")
print(data_csv)
