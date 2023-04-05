def matrixflip(m, s):
    f = []
    if s == 'h':
        for i in m:
            t = []
            for j in range(1, len(i)+1):
                t.append(i[-j])
            f.append(t)
        return f

    if s == 'v':
        for i in range(1, len(m)+1):
            f.append(m[-i])
        return f


myl = [[1, 2], [3, 4]]
print(matrixflip(matrixflip(myl, 'h'), 'v'))
