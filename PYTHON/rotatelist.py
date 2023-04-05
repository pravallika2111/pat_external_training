# Write a Python function rotatelist(l,k) that takes a list l and a positive
# integer k and returns the list l after k rotations. If k is not positive,
# your function should return l unchanged. Note that your function should not
# change l itself, and should return the rotated list.


def rotatelist(l, n):
    x = n % len(l)
    return l[x:]+l[:x]


l = [1, 2, 3, 4, 5]
n = 1
print(rotatelist(l, n))
