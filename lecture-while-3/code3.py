def myfind_while(l, v):
    '''return the smallest integer i such that l[i]=v,
    or -1 if v is not in l.

    '''
    i = 0
    while i < len(l) and l[i] != v:
        i += 1
    if i == len(l):
        return -1
    return i

def myfind(l, v):
    '''return the smallest integer i such that l[i]=v,
    or -1 if v is not in l.

    '''
    for i, e in enumerate(l):
        if e == v:
            return i
    return -1

def myrfind(l, v):
    '''return the largest integer i such that l[i]=v,
    or -1 if v is not in l.

    '''
    i = len(l) - 1 # start at largest i
    # while i < len(l) and l[i] != v:
    while i >= 0 and l[i] != v:#smallest allowed i is 0
        i -= 1 # step to the left in each iteration
    return i

def myfind_tests():
    '''test the myfind function'''

    # test 1
    l = [1, 2, 3]
    v = 2
    correct = 1 # since l[1] = 2
    ans = myfind(l, v)
    assert ans == correct, f'myfind test 1: expected {correct}, but got {ans}'

    # test 2
    l = ['foo', 'bar']
    v = 'bar'
    correct = 1 # since l[1] = 'bar'
    ans = myfind(l, v)
    assert ans == correct, f'myfind test 2: expected {correct}, but got {ans}'

    # test 3
    l = ['foo', 'bar']
    v = 'not in l'
    correct = -1
    ans = myfind(l, v)
    assert ans == correct, f'myfind test 3: expected {correct}, but got {ans}'

    print('myfind tests pass')

def myrfind_tests():
    '''test the myrfind function'''

    # test 1
    l = [1, 2, 3]
    v = 2
    correct = 1 # since l[1] = 2
    ans = myrfind(l, v)
    assert ans == correct, f'myrfind test 1: expected {correct}, but got {ans}'

    # test 2
    l = ['foo', 'bar']
    v = 'bar'
    correct = 1 # since l[1] = 'bar'
    ans = myrfind(l, v)
    assert ans == correct, f'myrfind test 2: expected {correct}, but got {ans}'

    # test 3
    l = ['foo', 'bar']
    v = 'not in l'
    correct = -1
    ans = myrfind(l, v)
    assert ans == correct, f'myrfind test 3: expected {correct}, but got {ans}'

    # test 4
    l = ['foo', 'bar', 'bar', 'baz']
    v = 'bar'
    correct = 2
    ans = myrfind(l, v)
    assert ans == correct, f'myrfind test 4: expected {correct}, but got {ans}'

    print('myrfind tests pass')

myfind_tests()
myrfind_tests()
