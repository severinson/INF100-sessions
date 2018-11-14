def main():
    lookup = dict()
    while True:
        print('Enter a name, or add to enter a new record.')
        s = input()
        if s == 'add': # handle adding new records
            print('Enter new name:')
            name = input()
            name = name.lower().strip() # normalize

            print('Enter number:')
            number = input()
            number = number.lower().strip() # normalize

            # store association in dict
            lookup[name] = number
        else: # lookup number of name
            name = s.lower().strip()
            if name in lookup:
                number = lookup[name]
                print(f'{name} has number {number}')
            else:
                print(f'No number stored for {name}')
        print()
main()
