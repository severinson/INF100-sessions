import csv

def load_tweets(filename='./tweets.csv'):
    result = dict()
    with open(filename) as f:
        reader = csv.DictReader(f)
        for tweet_dict in reader:
            tweet_id = tweet_dict['id_str']
            result[tweet_id] = tweet_dict
    return result

def count_by_device(tweets):
    result = dict()
    for tweet in tweets.values():
        device = tweet[0]
        if device not in result:
            result[device] = 0
        result[device] += 1
    return result

def count_by_hour(tweets):
    result = dict()
    for tweet in tweets.values():
        date_time = tweet['created_at']
        date_time_split = date_time.split(' ')
        if len(date_time_split) != 2:
            continue
        _, time = date_time_split
        hour, _, _ = time.split(':')
        hour = int(hour)
        result[hour] = result.get(hour, 0) + 1
    return result

tweets = load_tweets()
# by_device = count_by_device(tweets)
# # print(by_device)
by_hour = count_by_hour(tweets)
# # print(by_hour)

# convert to lists
hours = list(by_hour)
ntweets = list(by_hour.values())
print(hours)
print(ntweets)

import matplotlib.pyplot as plt
plt.figure()
plt.plot(hours, ntweets, '.')
plt.show()
