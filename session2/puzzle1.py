def g():
    return 10

def f():
    a = 10
    return g() * 2

result = f()
print('result of f is', result)
result = g()
print('result of g is', result)
