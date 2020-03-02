from os import listdir
from os.path import isfile, join

mypath = "russian-troll-tweets-master"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

files = [mypath+"//"+i for i in onlyfiles]
frames = []

for i in files:
    df = pd.read_csv(i)
    frames.append(df)

import pandas as pd
df = pd.concat(frames)
