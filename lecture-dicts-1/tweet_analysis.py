import csv

def load_tweets():
    filename = 'tweets.csv'
    tweets = dict()
    with open(filename) as f:
        reader = csv.reader(f)
        for tweet in reader:
            tweet_id = tweet[-1]
            tweets[tweet_id] = tweet
    return tweets

def count_by_device(tweets):
    '''count the number of tweets associated with each device.'''
    by_device = dict()
    for tweet_id in tweets:
        tweet = tweets[tweet_id]
        device = tweet[0]

        # count occurrences
        by_device[device] = by_device.get(device, 0) + 1

    return by_device

def count_by_word(tweets):
    '''count the number of times each word is used in any tweet.'''
    result = dict()
    for tweet_id in tweets:
        tweet = tweets[tweet_id]
        text = tweet[1]

        # count words
        for word in text.split(' '):
            word = word.strip().lower()
            result[word] = result.get(word, 0) + 1

    return result

tweets = load_tweets()
by_device = count_by_device(tweets)
print(by_device)

by_word = count_by_word(tweets)
l = list(by_word.items())
l.sort(key=lambda x: x[1])
counts = [v[1] for v in l]
counts.reverse()

import matplotlib.pyplot as plt
plt.figure()
plt.loglog(counts)
plt.show()

# for word, count in by_word.items():
#     print(f'{word}: {count}')

# for tweet_id in tweets:
#     print(tweet_id)
#     tweet = tweets[tweet_id]
#     print(tweet)
#     print()
