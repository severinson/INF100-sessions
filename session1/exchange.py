def exchange(nok, currency):
    rate = 0
    if currency == 'btc':
        rate = 0.000017
    elif currency == 'doge':
        rate = 22.88
    else:
        print(currency, 'not recognized!')
        return 'undefined'
    print('exchange rate for', currency, 'is', rate)
    result = nok * rate
    return result

i = 0
while i < 4:
    print('run', i, 'of the loop')
    i = i + 1

    nok = -1
    while nok <= 0:
        print('enter amount of nok (> 0):')
        nok = float(input())

    print('enter currency to convert to')
    currency = input()
    currency = currency.lower() # make lower case

    result = exchange(nok, currency)
    print(nok, 'nok converted to', currency, ':', result)
    print()

print('program exists normally')
