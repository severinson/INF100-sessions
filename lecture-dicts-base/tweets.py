import csv

from collections import defaultdict

def load_tweets(filename='tweets.csv'):
    d = dict()
    with open(filename) as csvfile:
        for tweet in csv.reader(csvfile):
            tweet_id = tweet[-1]
            d[tweet_id] = tweet
    return d

def count_devices(tweets):
    by_device = dict()
    for tweet_id in tweets:
        tweet = tweets[tweet_id]
        device = tweet[0]
        by_device[device] = by_device.get(device, 0) + 1
    return by_device

def count_words(tweets):
    by_word = defaultdict(int)
    for tweet_id in tweets:
        tweet = tweets[tweet_id]
        text = tweet[1].lower()
        for word in text.split(' '):
            by_word[word] += 1
    return by_word

d = load_tweets()
by_device = count_devices(d)
print(by_device)

by_word = count_words(d)
# print(by_word)
word_list = list(by_word.items())
word_list.sort(key=lambda x: x[1])
for word in word_list:
    print(word)

import matplotlib.pyplot as plt
word_list.reverse()
occurrences = [x[1] for x in word_list]

plt.figure()
plt.loglog(occurrences)
plt.show()
