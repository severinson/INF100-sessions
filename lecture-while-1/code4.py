def myfind_while(l, v):
    '''return the smallest i such that l[i]=v
    or -1 if v is not in l.

    '''
    i = 0
    while i < len(l) and l[i] != v:
        i += 1

    # runs if v isn't in l
    if i == len(l):
        return -1

    return i

def myfind(l, v):
    '''return the smallest i such that l[i]=v
    or -1 if v is not in l.

    '''
    for i, e in enumerate(l):
        if e == v:
            return i
    return -1

def myrfind(l, v):
    '''return the largest i such that l[i]=v
    or -1 if v is not in l.

    '''
    i = len(l) - 1
    while i > -1 and l[i] != v:
        i -= 1
    return i

def test_myfind():
    '''test the myfind function'''

    # test 1
    l = [1, 2, 3]
    v = 1
    correct = 0 # since l[0] = 1
    i = myfind(l, v)
    assert i == correct, f'myfind test 1 expected {correct}, got {i}'

    # test 2
    l = [1, 2, 3]
    v = 2
    correct = 1 # since l[1] = 2
    i = myfind(l, v)
    assert i == correct, f'myfind test 2 expected {correct}, got {i}'

    # test 3
    l = [1, 2, 3]
    v = 'not in list'
    correct = -1
    i = myfind(l, v)
    assert i == correct, f'myfind test 3 expected {correct}, got {i}'

    # test 4
    l = []
    v = None
    correct = -1
    i = myfind(l, v)
    assert i == correct, f'myfind test 4 expected {correct}, got {i}'

    # test 5
    l = ['foo', 'bar', 'baz', 'baz']
    v = 'baz'
    correct = 2
    i = myfind(l, v)
    assert i == correct, f'myfind test 5 expected {correct}, got {i}'

    print('myfind tests pass')

def test_myrfind():
    '''test the myrfind function'''

    # test 1
    l = [1, 2, 3]
    v = 1
    correct = 0 # since l[0] = 1
    i = myrfind(l, v)
    assert i == correct, f'myrfind test 1 expected {correct}, got {i}'

    # test 2
    l = [1, 2, 3]
    v = 2
    correct = 1 # since l[1] = 2
    i = myrfind(l, v)
    assert i == correct, f'myrfind test 2 expected {correct}, got {i}'

    # test 3
    l = [1, 2, 3]
    v = 'not in list'
    correct = -1
    i = myrfind(l, v)
    assert i == correct, f'myrfind test 3 expected {correct}, got {i}'

    # test 4
    l = []
    v = None
    correct = -1
    i = myrfind(l, v)
    assert i == correct, f'myrfind test 4 expected {correct}, got {i}'

    # test 5
    l = ['foo', 'bar', 'baz', 'baz']
    v = 'baz'
    correct = 3
    i = myrfind(l, v)
    assert i == correct, f'myrfind test 5 expected {correct}, got {i}'

    print('myrfind tests pass')

test_myfind()
test_myrfind()
