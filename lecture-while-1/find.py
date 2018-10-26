# i = 0
# while i < 10:
#     print(f'i={i}')
#     i += 1
# print(f'loop finished at i={i}')

def myfind_while_1(l, v):
    '''return the index of the first element of l equal to v or -1 if v
    isn't in l.

    '''
    i = 0
    while l[i] != v:
        i += 1
    return i

def myfind_while_1(l, v):
    '''return the index of the first element of l equal to v or -1 if v
    isn't in l.

    '''
    if not l:
        return -1
    i = 0
    while l[i] != v:
        i += 1
    return i

def myfind_while_3(l, v):
    '''return the index of the first element of l equal to v or -1 if v
    isn't in l.

    '''
    i = 0
    while l[i] != v and i < len(l):
        i += 1
    if i == len(l):
        return -1
    return i

def myfind_while(l, v):
    '''return the index of the first element of l equal to v or -1 if v
    isn't in l.

    '''
    if not l:
        return -1
    i = 0
    while i < len(l) and l[i] != v:
        i += 1
    if i == len(l):
        return -1
    return i

def myfind_for_1(l, v):
    '''return the index of the first element of l equal to v or -1 if v
    isn't in l.

    '''
    i = 0
    for e in l:
        if e == v:
            return i
        i += 1
    return -1

def myfind_for_2(l, v):
    '''return the index of the first element of l equal to v or -1 if v
    isn't in l.

    '''
    for i, e in enumerate(l):
        if e == v:
            return i
        i += 1
    return -1

myfind = myfind_for_2

def test_myfind():
    '''test the myfind function'''

    # test 1
    l = [1, 2, 3]
    v = 2
    i = myfind(l, v)
    correct = 1
    assert i == correct, f'myfind test 1 failure. expected {correct}, got {i}.'

    # test 2
    l = ['foo', 'bar', 'baz', 'bax']
    v = 'baz'
    i = myfind(l, v)
    correct = 2
    assert i == correct, f'myfind test 2 failure. expected {correct}, got {i}.'

    # test 3
    l = []
    v = None
    i = myfind(l, v)
    correct = -1
    assert i == correct, f'myfind test 3 failure. expected {correct}, got {i}.'

    # test 4
    l = ['foo', 'bar', 'baz', 'bax']
    v = 'notinlist'
    i = myfind(l, v)
    correct = -1
    assert i == correct, f'myfind test 4 failure. expected {correct}, got {i}.'

    # test 5
    l = ['foo', 'bar', 'baz', 'baz']
    v = 'notinlist'
    i = myfind(l, v)
    correct = -1
    assert i == correct, f'myfind test 5 failure. expected {correct}, got {i}.'

    # test 6
    l = ['foo', 'bar', 'baz', 'baz']
    v = 'baz'
    i = myfind(l, v)
    correct = 2
    assert i == correct, f'myfind test 5 failure. expected {correct}, got {i}.'

    print('all tests pass for myfind')

def myrfind(l, v):
    '''return the largest index i such that l[i]=v or -1 if v isn't in l.

    '''
    if not l:
        return -1
    i = len(l) - 1 # start with only i = len(l)
    while i >= 0 and l[i] != v: # start with only l[i] != v
        i -= 1
    if i == -1:
        return -1
    return i

def test_myrfind():
    '''test the myrfind function'''

    # test 1
    l = [1, 2, 3]
    v = 2
    i = myrfind(l, v)
    correct = 1
    assert i == correct, f'myrfind test 1 failure. expected {correct}, got {i}.'

    # test 2
    l = ['foo', 'bar', 'baz', 'bax']
    v = 'baz'
    i = myrfind(l, v)
    correct = 2
    assert i == correct, f'myrfind test 2 failure. expected {correct}, got {i}.'

    # test 3
    l = []
    v = None
    i = myrfind(l, v)
    correct = -1
    assert i == correct, f'myrfind test 3 failure. expected {correct}, got {i}.'

    # test 4
    l = ['foo', 'bar', 'baz', 'bax']
    v = 'notinlist'
    i = myrfind(l, v)
    correct = -1
    assert i == correct, f'myrfind test 4 failure. expected {correct}, got {i}.'

    # test 5
    l = ['foo', 'bar', 'baz', 'baz']
    v = 'notinlist'
    i = myrfind(l, v)
    correct = -1
    assert i == correct, f'myrfind test 5 failure. expected {correct}, got {i}.'

    # test 6
    l = ['foo', 'bar', 'baz', 'baz']
    v = 'baz'
    i = myrfind(l, v)
    correct = 3
    assert i == correct, f'myrfind test 5 failure. expected {correct}, got {i}.'

    print('all tests pass for myrfind')

if __name__ == '__main__':
    test_myfind()
    test_myrfind()
