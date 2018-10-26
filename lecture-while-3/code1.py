# i = 0
# cond = i < 10
# while cond:
#     print(f'i={i}')
#     i += 1
#     cond = i < 10

cond = True
while cond:
    print()
    print('Give me something!')
    s = input()
    if not s:
        # break
        # if s == 'exit':
        cond = False
    print(f'You gave me {s}')

print('program exits here')
