print('Program starts')

def strlen(s):
    '''return the length of the string s.'''
    assert isinstance(s, str), 'strlen only takes string arguments'
    return len(s)

# s = 'foobar'
s = 10
l = strlen(s)
print(f'len of string s is {l}')

print('Program reached its final line.')
