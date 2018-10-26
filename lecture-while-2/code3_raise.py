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
    i = 0
    for i, e in enumerate(l):
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

test_myfind()
