while True:
    print('Please give me something: ')
    s = input()

    # handle exit command
    if s == 'exit':
        break

    print('You gave me', s)

print('Program exits')
