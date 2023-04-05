# Write a function matched(s) that takes as input a string s and checks if the
# brackets "(" and ")" in s are matched: that is, every "(" has a matching ")" 
# after it and every ")" has a matching "(" before it. Your function should
# ignore all other symbols that appear in s. Your function should return True
# if s has matched brackets and False if it does not.

def matched(s):
    a = []
    for i in s:
        if i == ')' and len(a) == 0:
            return False
        if i == '(':
            a.append(i)
        elif i == ')':
            a.pop()

    if len(a) == 0:
        return True
    else:
        return False


s = "a(d(DI()))a()a()AAa((a))"
print(matched(s))
