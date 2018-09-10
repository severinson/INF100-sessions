'''My solution to weekly problem 2.

'''

def quota1(nadults):
    return nadults * 0.3

def quota2(nchicks, nadults):
    rate = 0
    if nchicks < nadults * 0.2:
        rate = 0.1
    else:
        rate = 0.3
    return nadults * rate

def quota3(nchicks, nadults):
    if nchicks < nadults * 0.1:
        return 0
    if nchicks < nadults * 0.2:
        return nadults * 0.1
    return nadults * 0.3

def simulate1(nage0, nage1, nage2, nadults):
    '''
    returns the number of adult Puffins at the end of the year
    based on the number of Puffins at the beginning of the year.

    args:

    nage0: number of Puffins at age 0 (newborns)

    nage1, nage2: number of Puffins of age 1, 2.

    nadult: number of adult Puffins.

    returns: the number of adult Puffins at the end of the year.
    '''
    nchiks = nage0 + nage1 + nage2
    hunted = quota3(nchiks, nadults) # number of hunted adults
    nadults -= hunted # equal to nadults = nadults - hunted
    nadults += nage2 #nage2 puffins become adults by end of year
    return nadults

def deathrate1(npuffins, age):
    '''return the estimated number of Puffins of a given age
    that die in each year due to natural causes.
    '''
    if age == 0:
        return npuffins * 0.2
    if age == 1:
        return npuffins * 0.05
    if age == 2:
        return npuffins * 0.01
    if age == 3:
        return npuffins * 0.002
    return None

def deathrate2(npuffins, age, ntotal):
    '''return the estimated number of Puffins of a given age
    that die in each year due to natural causes. takes into account
    food scarcity causes by the population growing too large.

    '''
    result = 0

    # handle deahtrate for different ages
    if age == 0:
        result = npuffins * 0.2
    elif age == 1:
        result = npuffins * 0.05
    elif age == 2:
        result = npuffins * 0.01
    elif age == 3:
        result = npuffins * 0.002
    else:
        raise ValueError('age must be in [0, 1, 2, 3] but is {}'.format(age))

    # handle overpopulation
    if ntotal > 10000:
        result *= ntotal / 10000
    return result

def deathrate3(npuffins, age, ntotal):
    '''return the estimated number of Puffins of a given age
    that die in each year due to natural causes. takes into account
    food scarcity causes by the population growing too large.
    '''
    result = 0

    # handle deahtrate for different ages
    if age == 0:
        result = npuffins * 0.2
    elif age == 1:
        result = npuffins * 0.05
    elif age == 2:
        result = npuffins * 0.01
    elif age == 3:
        result = npuffins * 0.002
    else:
        raise ValueError('age must be in [0, 1, 2, 3] but is {}'.format(age))

    # handle overpopulation
    if ntotal > 10000:
        result *= ntotal / 10000
    return min(result, npuffins)

def simulate2(nage0, nage1, nage2, nadults):
    '''
    returns the number of adult Puffins at the end of the year
    based on the number of Puffins at the beginning of the year.
    takes death rate into account.

    args:

    nage0: number of Puffins at age 0 (newborns)

    nage1, nage2: number of Puffins of age 1, 2.

    nadult: number of adult Puffins.

    returns: the number of adult Puffins at the end of the year.
    '''
    nchicks = nage0 + nage1 + nage2
    nadults -= quota3(nchicks, nadults)
    ntotal = nage0 + nage1 + nage2 + nadults
    nadults -= deathrate3(nadults, 3, ntotal)
    nage2 -= deathrate3(nage2, 2, ntotal)
    nadults += nage2
    return nadults

def nsimulate(years, nage0, nage1, nage2, nadults):
    '''
    returns the number of adult Puffins at the end of years years
    based on the number of Puffins at the beginning of the year 0.
    takes death rate into account.

    args:

    years: the number of years to simulate.

    nage0: number of Puffins at age 0 (newborns) at the beginning of year 0.

    nage1, nage2: number of Puffins of age 1, 2 at the beginning of year 0.

    nadult: number of adult Puffins at the beginning of year 0.

    returns: the number of adult Puffins after years years.
    '''
    for i in range(years):
        nchicks = nage0 + nage1 + nage2
        nadults -= quota3(nchicks, nadults)
        ntotal = nage0 + nage1 + nage2 + nadults
        nadults -= deathrate3(nadults, 3, ntotal)
        nage0 -= deathrate3(nage0, 0, ntotal)
        nage1 -= deathrate3(nage1, 1, ntotal)
        nage2 -= deathrate3(nage2, 2, ntotal)
        nadults += nage2
        nage2 = nage1
        nage1 = nage0
        nage0 = nadults * 0.4

    return nadults

# run nsimulate
nadults = nsimulate(10, 10, 11, 15, 32)
print('nadults is', nadults)
