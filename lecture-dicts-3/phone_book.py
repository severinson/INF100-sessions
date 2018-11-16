def main():
    number_table = dict()
    while True:
        print('Enter a name, or add to register a new number')
        s = input()

        # handle adding a new entry to the phone book
        if s == 'add':
            print('Enter new name:')
            name = input()
            name = name.lower().strip() # normalize

            print(f'Enter number of {name}')
            number = input()
            number = number.lower().strip()

            # store association
            number_table[name] = number
        else: # handle number lookup
            name = s.lower().strip()
            if name in number_table:
                number = number_table[name]
                print(f'{s} has number {number}')
            else:
                print(f'No number associated with {s}')
        print()
    return
main()
