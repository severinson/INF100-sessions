def noccurrences_1(l):
    '''return a dict mapping each unique element in l to the number of
    times it occurs in l.

    '''
    result = dict()
    for v in l:
        if v not in result:
            result[v] = 0
        result[v] += 1
    return result

def noccurrences_2(l):
    '''return a dict mapping each unique element in l to the number of
    times it occurs in l.

    '''
    result = dict()
    for v in l:
        result[v] = result.get(v, 0) + 1
    return result

from collections import defaultdict
def noccurrences(l):
    '''return a dict mapping each unique element in l to the number of
    times it occurs in l.

    '''
    result = defaultdict(int)
    for v in l:
        result[v] += 1
    return result

def tests():
    l = [1, 2, 3, 1]
    ans = noccurrences(l)
    correct = {1: 2, 2: 1, 3: 1}
    assert ans == correct, f'expected {correct}, but got {ans}'

    s = 'foo'
    ans = noccurrences(s)
    correct = {'f': 1, 'o': 2}
    assert ans == correct, f'expected {correct}, but got {ans}'

    print('tests pass')
tests()
