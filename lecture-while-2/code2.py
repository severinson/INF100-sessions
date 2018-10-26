print('program starts here')

def intsum(a, b):
    '''add two integers a and b'''
    assert isinstance(a, int), f'a must be int, but is {type(a)}'
    assert isinstance(b, int), f'b must be int, but is {type(b)}'
    return a + b

a = 10
b = 'foo'
result = intsum(a, b)
print('result is', result)

print('program exits here')
