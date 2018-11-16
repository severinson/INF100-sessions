def noccurrences_1(l):
    '''return a dict mapping each unique element in l
    to the number of times that element occurrs in l.

    '''
    result = dict() # create a new dict
    for v in l: # loop over elements in l
        if v not in result: # handle v not in result
            result[v] = 0
        result[v] += 1 # count elements
    return result

def noccurrences_2(l):
    '''return a dict mapping each unique element in l
    to the number of times that element occurrs in l.

    '''
    result = dict() # create a new dict
    for v in l: # loop over elements in l
        result[v] = result.get(v, 0) + 1
    return result

from collections import defaultdict
def noccurrences(l):
    '''return a dict mapping each unique element in l
    to the number of times that element occurrs in l.

    '''
    result = defaultdict(int) # create a new dict
    for v in l: # loop over elements in l
        result[v] += 1
    return result

def tests():
    l = [1, 2, 3, 1, 2]
    correct = {
        1: 2,
        2: 2,
        3: 1,
    }
    ans = noccurrences(l)
    assert ans == correct, f'expected {correct}, but got {ans}'

    l = ['foo', 'bar', 'foo']
    correct = {
        'foo': 2,
        'bar': 1
    }
    ans = noccurrences(l)
    assert ans == correct, f'expected {correct}, but got {ans}'

    print('all tests pass')

tests()
