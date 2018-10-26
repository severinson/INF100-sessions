print('program starts')

def intsquare(a):
    '''return the square of integer a'''
    assert isinstance(a, int), 'input a of intsquare must be of type int'
    return pow(a, 2)

a = 'foo'
result = intsquare(a)
print(f'result is {result}')

print('program exits')
