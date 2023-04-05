# Define a Python function remdup(l) that takes a nonempty list of integers l and removes all duplicates in l, keeping only the last occurrence of each number.

def remdup(l):
    for i in range(len(l)):
        if l[0] in l[1:]:
            l.remove(l[0])

    return l


l = [3, 5, 7, 5, 3, 7, 10]

print(remdup(l))
