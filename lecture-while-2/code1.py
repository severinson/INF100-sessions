# i = 0
# while i < 10:
#     print(f'i={i}')
#     i += 1

cond = True
while cond:
    print()
    print('Give me something: ')
    s = input()

    # handle exit condition
    if s == 'exit':
        cond = False

    print('You gave me:', s)

print('program exists here')
