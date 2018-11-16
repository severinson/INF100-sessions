import csv

def load_tweets(filename='./tweets.csv'):
    with open(filename) as f:
        reader = csv.DictReader(f)
        return list(reader)

def count_by_hour(tweets):
    '''return a dict mapping each hour to the number
    of tweets in that hour.

    '''
    result = dict()
    for hour in range(0, 24):
        result[hour] = 0
    for tweet in tweets:
        created_at = tweet['created_at']
        # created_at has format '06-21-2018 20:45:32'
        _, time = created_at.split(' ')
        hour, _, _ = time.split(':')
        hour = int(hour) # convert to int
        result[hour] += 1
    return result

tweets = load_tweets()
by_hour = count_by_hour(tweets)
l = list(by_hour.items())
hours = [x[0] for x in l]
ntweets = [x[1] for x in l]

import matplotlib.pyplot as plt
plt.figure()
plt.plot(hours, ntweets,  '-')
plt.xlabel('hour')
plt.ylabel('#tweets')
plt.grid()
plt.show()
