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
