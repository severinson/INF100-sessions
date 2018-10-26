def main():
    running = True
    while running:
        s = input()
        print('You entered', s)
        s = s.lower().strip()
        if s == 'exit':
            running = False
    print('exiting')

main()
