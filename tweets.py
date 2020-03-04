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
    df = pd.read_csv(i,error_bad_lines=False)
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

tag_df = pd.DataFrame({"tag":tags,"test":"test"})
hash_df = pd.DataFrame({"hash":hashtags,"test":"test"})

count_t = tag_df.groupby(by="tag").count().sort_values(by="test",ascending=False)
count_h = hash_df.groupby(by="hash").count().sort_values(by="test",ascending=False)

count_t.to_csv("tag.csv")
count_h.to_csv("hash.csv")

n = 2
for i in range(2,6):
    array =[]
    array2 =[]
    print('getting',i)
    bgs = nltk.ngrams(tokens,i)
    print('grams',i)
    fdist = nltk.FreqDist(bgs)
    print('dist',i)
    for k,v in fdist.items():
        if v >10:
            array.append(k)
            array2.append(v)
            print("got")
    print('array',i)
    array1 = []
    for i in range(len(array)):
        x = ' '.join(map(str,array[i]))
        array1.append(x)
    print('framing',i)
    df = pd.DataFrame({'phrase':array1,'count': array2}).sort_values(by="count",ascending=False)
    df.to_csv(str(n)+'_grams.csv')
    n+=1
