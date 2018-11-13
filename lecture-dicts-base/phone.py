def main():
    phone_book = dict()
    while True:
        print('Enter a name or enter add to add a new entry.')
        command = input().strip()
        if command == 'add':
            print('Enter name:')
            name = input().strip().lower()
            print('Enter number:')
            number = input().strip()
            phone_book[name] = number
        else:
            name = command.lower()
            if name not in phone_book:
                print(f'No entry for {command}.')
                continue
            number = phone_book[name]
            print(f'{name}\'s number is {number}.')
    return

main()
