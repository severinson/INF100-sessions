def main():
    lookup = dict()
    while True:
        print('Enter a name, or add to add a new entry.')
        s = input().strip()
        if s == 'add':

            # get entry details from user
            print('Enter name for new entry:')
            name = input().strip().lower()
            print('Enter phone number:')
            number = input()

            # store number associated with name
            lookup[name] = number
        elif s == 'exit':
            return # close program
        else:

            # normalize input
            name = s.lower()

            # lookup association
            if name in lookup:
                number = lookup[name]
                print(f'Number for {name} is {number}')
            else:
                print(f'No number associated with {name}.')
        print('----------------------')
        print()
    return

main()
