from collections import defaultdict

def noccurrences_1(l):
    '''return a dict mapping each unique element in l to the number of
    times that element occurs in l. For example, if l = 'foo', this
    function returns {'f': 1, 'o': 2}.

    '''
    result = dict()
    for v in l:
        if v not in result:
            result[v] = 0
        result[v] += 1
    return result

def noccurrences_2(l):
    '''return a dict mapping each unique element in l to the number of
    times that element occurs in l. For example, if l = 'foo', this
    function returns {'f': 1, 'o': 2}.

    '''
    result = dict()
    for v in l:
        result[v] = result.get(v, 0) + 1
    return result

def noccurrences(l):
    '''return a dict mapping each unique element in l to the number of
    times that element occurs in l. For example, if l = 'foo', this
    function returns {'f': 1, 'o': 2}.

    '''
    result = defaultdict(int)
    for v in l:
        result[v] += 1
    return result

def tests():
    '''test te noccurrences function.'''
    s = 'foo'
    ans = noccurrences(s)
    correct = {'f': 1, 'o': 2}
    assert len(ans) == 2
    assert ans['f'] == 1
    assert ans['o'] == 2

    print('all tests pass')

tests()
