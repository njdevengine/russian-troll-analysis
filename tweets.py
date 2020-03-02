from os import listdir
from os.path import isfile, join
import nltk, re, pprint
from nltk import word_tokenize
import pandas as pd

mypath = "russian-troll-tweets-master"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

files = [mypath+"//"+i for i in onlyfiles]
frames = []

for i in files:
    df = pd.read_csv(i)
    frames.append(df)

df = pd.concat(frames)

df2 = df[df.language =="English"]

tweets = list(set(list(df2.content)))

clean_tweets = []
for i in tweets:
    if type(i) != float:
        clean_tweets.append(i)
        
tweet_string = " ".join(clean_tweets)
tokens = word_tokenize(tweet_string)
text = nltk.Text(tokens)

#collocations = text.collocations()
#text.similar("Trump")

import nltk
from nltk.book import *
fdist = FreqDist(text)

#fdist.most_common(10)

my_set = set(text)
long_words = [word for word in my_set if len(word) > 15]
#sorted(long_words)

filtered_array = sorted(set(word.lower() for word in text if word.isalpha() and len(word)>3))

tags = []
hashtags = []
for i in range(len(clean_tweets)):
    if "@" in clean_tweets[i]:
        for n in clean_tweets[i].split(" "):
            if "@" in n:
                tags.append(n)
                
for i in range(len(clean_tweets)):
    if "#" in clean_tweets[i]:
        for n in clean_tweets[i].split(" "):
            if "#" in n:
                hashtags.append(n)     
                
tag_df = pd.DataFrame({"tag":tags})
hash_df = pd.DataFrame({"hash":hashtags})
tag_df.to_csv("tag.csv")
hash_df.to_csv("hash.csv")
