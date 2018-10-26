def myfind_while(l, v):
    '''return the smallest i such that l[i]=v,
    or -1 if v is not in l.

    '''
    i = 0
    while i < len(l) and l[i] != v:
        i += 1
    if i == len(l):
        return -1
    return i

def myfind(l, v):
    '''return the smallest i such that l[i]=v,
    or -1 if v is not in l.

    '''
    for i, e in enumerate(l):
        if e == v:
            return i
    return -1

def myrfind_while(l, v): # < edit this function
    '''return the largest i such that l[i]=v,
    or -1 if v is not in l.

    '''
    i = len(l)-1 # start with the largest index
    while i >= 0 and l[i] != v:
        i -= 1 # go down 1 on each iteration
    return i

def myrfind(l, v):
    '''return the largest i such that l[i]=v,
    or -1 if v is not in l.

    '''
    pairs = list(enumerate(l))
    pairs.reverse()
    for i, e in pairs:
        if e == v:
            return i
    return -1

def test_myfind():

    # test 1
    l = [1, 2, 3]
    v = 2
    correct = 1 # since l[1] = 2
    ans = myfind(l, v)
    assert ans == correct, f'myfind test 1: expected {correct}, but got {ans}'

    # test 2
    l = [1, 2, 3]
    v = 'notinlist'
    correct = -1
    ans = myfind(l, v)
    assert ans == correct, f'myfind test 2: expected {correct}, but got {ans}'

    # test 3
    l = []
    v = None
    correct = -1
    ans = myfind(l, v)
    assert ans == correct, f'myfind test 3: expected {correct}, but got {ans}'

    print('myfind tests pass')

def test_myrfind():

    # test 1
    l = [1, 2, 3]
    v = 2
    correct = 1 # since l[1] = 2
    ans = myrfind(l, v)
    assert ans == correct, f'myrfind test 1: expected {correct}, but got {ans}'

    # test 2
    l = [1, 2, 3]
    v = 'notinlist'
    correct = -1
    ans = myrfind(l, v)
    assert ans == correct, f'myrfind test 2: expected {correct}, but got {ans}'

    # test 3
    l = []
    v = None
    correct = -1
    ans = myrfind(l, v)
    assert ans == correct, f'myrfind test 3: expected {correct}, but got {ans}'

    # test 4
    l = ['foo', 'baz', 'baz', 'bar']
    v = 'baz'
    correct = 2
    ans = myrfind(l, v)
    assert ans == correct, f'myrfind test 4: expected {correct}, but got {ans}'

    print('myrfind tests pass')

test_myfind()
test_myrfind()
