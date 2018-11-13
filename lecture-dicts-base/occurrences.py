from collections import defaultdict

def noccurrences_1(l):
    '''count the number of occurrences of each element in l.'''
    d = dict()
    for v in l:
        if v not in d:
            d[v] = 0
        d[v] += 1
    return d

def noccurrences_2(l):
    '''count the number of occurrences of each element in l.'''
    d = dict()
    for v in l:
        d[v] = d.get(v, 0) + 1
    return d

def noccurrences(l):
    '''count the number of occurrences of each element in l.'''
    d = defaultdict(int)
    for v in l:
        d[v] += 1
    return d

def tests():
    s = 'foo'
    ans = noccurrences(s)
    assert len(ans) == 2
    assert ans['f'] == 1
    assert ans['o'] == 2

    l = [1, 2, 3, 1, 2, 10]
    ans = noccurrences(l)
    assert len(ans) == 4
    assert ans[1] == 2
    assert ans[2] == 2
    assert ans[3] == 1
    assert ans[10] == 1

    print('all tests pass')

tests()
