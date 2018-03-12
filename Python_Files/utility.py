import os
import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud
from collections import defaultdict

def create_bow_rep( in_tweet ):
    bow_map = defaultdict(int)
    tokens = in_tweet.split()
    for tok in tokens:
        bow_map[tok] += 1
    return bow_map

def load_hashtag(data_location, htf):
    tweets = []
    labels = []
    for line in open(os.path.join(data_location,htf)).readlines():
        line_split = line.strip().split('\t')
        tweets.append(line_split[1])
        labels.append(int(line_split[2]))

    Y = np.array(labels)
    X_bow = [create_bow_rep(tweet) for tweet in tweets]

    return {'X_bow':X_bow,'Y':Y}


def create_data(data_location):
    ht_files = sorted(os.listdir(data_location))

    Xs = []
    ys = []
    ht_list = []
    for htf in ht_files:
        ht_dict = load_hashtag(data_location,htf)

        ht_list.append(htf)
        ys.append(ht_dict['Y'])
        Xs.append(ht_dict['X_bow'])

    return Xs, ys, ht_list

def avg_len(dic, label):
    count = 0
    for i in range(len(dic)):
        if label[i] != 0:
            for key in dic[i].keys():
                if key[0] not in ['#', '@']:
                      count += dic[i][key]
                if key[0] == '#':
                    hsh = key
    return count/10.0, hsh

def wordcloud(dic):
    words = []
    for X in dic:
        for word in X.keys():
            if word[0] not in ['#', '@'] and word not in ['https', 'Https', 'http']:
                   words.append(word)
            if word[0] == '#':
                hsh = word
    
    wordcloud = WordCloud().generate((' '.join(words)))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.xlabel(hsh)
    plt.axis("off")
    
    return hsh
    