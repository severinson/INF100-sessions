def findsorted(l, v):
    '''find the smallest i such that l[i]=v
    or 1 if v is not in l.

    assumes that l is sorted.

    '''
    print('findsorted called')

    # initialize i to the midpoint of the list
    lower = 0
    upper = len(l)
    midpoint = int(len(l) / 2)
    while l[midpoint] != v:
        midpoint = int(lower + (upper-lower) / 2)
        if l[midpoint] > v:
            upper = midpoint
        elif l[midpoint] < v:
            lower = midpoint

    return midpoint

def test_findsorted():
    l = list(range(10000000))
    v = len(l) - 1
    correct = len(l) - 1
    i = findsorted(l, v)
    assert i == correct, f'findsorted test 1 expected {correct}, got {i}'

    print('findsorted tests pass')

test_findsorted()
