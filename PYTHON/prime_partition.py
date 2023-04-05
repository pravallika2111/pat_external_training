# Write a Python function primepartition(m) that takes an integer m as input
# and returns True if m can be partitioned as primes and False otherwise.
# (If m is not positive, your function should return False.)

def primepartition(m):
    if m > 0:
        primelist = []
        for i in range(2, m + 1):
            for p in range(2, int(m**0.5)):
                if (i % p) == 0:
                    break
            else:
                primelist.append(i)

        for x in primelist:
            y = m-x
            if y in primelist:
                return True
        return False
    else:
        return False


m = 7
print(primepartition(m))
