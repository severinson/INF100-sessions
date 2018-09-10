# you may may need to install this module separately.
# if you're using Anaconda (not miniconda) it should already be installed.
import matplotlib.pyplot as plt

def quota3(nchicks, nadults):
    if nchicks < nadults * 0.1:
        return 0
    if nchicks < nadults * 0.2:
        return nadults * 0.1
    return nadults * 0.3

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
    result = list()
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
        result.append(nadults)

    return result

# result = nsimulate(10, 10, 11, 15, 32)
result = nsimulate(12, 100, 2, 3, 400)
plt.plot(result)
print('result is', result)
plt.ylabel('nadults')
plt.xlabel('year')
plt.show()
