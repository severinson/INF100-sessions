def f(l):
    l[0] += 10
    print('l in function is', l)

l = [1,2,3]
f(l)
print('l after function is', l)
