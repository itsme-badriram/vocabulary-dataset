from PyDictionary import PyDictionary
dictionary=PyDictionary()


import pandas as pd
import numpy as np
df = pd.read_csv('vocabulary.csv')

df = np.array(df)
setA = df.T[0]
setB = df.T[1]
setC = df.T[2]
setD = df.T[3]
setE = df.T[4]



levelD = []
for a in setD:
        syns = dictionary.synonym(a)
        ans = dictionary.antonym(a)
        if (ans == None):
            ans = []
        if (syns == None):
            continue
        A = {}
        A['word'] = a
        A['synonyms'] = syns
        A['antonyms'] = ans
        levelD.append(A)

levelE = []
for b in setE:
        syns = dictionary.synonym(b)
        ans = dictionary.antonym(b)
        if (ans == None):
            ans = []
        if (syns == None):
            continue
        A = {}
        A['word'] = b
        A['synonyms'] = syns
        A['antonyms'] = ans
        levelE.append(A)

levelC = []
for b in setC:
        syns = dictionary.synonym(b)
        ans = dictionary.antonym(b)
        if (ans == None):
            ans = []
        if (syns == None):
            continue
        A = {}
        A['word'] = b
        A['synonyms'] = syns
        A['antonyms'] = ans
        levelC.append(A)

np.save('levelA.npy', levelA) 



np.save('levelE.npy', levelE) 
a = np.load('levelE.npy',  allow_pickle=True)

i=0
step = 10
l = len(a)
counter = 0
levels = []
while (i < l ):
    if (step < 60):
        step = step + (counter * 10)
    else:
        step = step + 5
    if (i+step > l):
        words = a[i:l]
        levelTemp = {}
        levelTemp['level'] = counter + 1
        levelTemp['words'] = words.tolist()
        levels.append(levelTemp)
        break
    words = a[i:i+step]
    i = i + step
    levelTemp = {}
    levelTemp['level'] = counter + 1
    levelTemp['words'] = words.tolist()
    levels.append(levelTemp)
    counter = counter + 1
   
import json
lists = levels
json_str = json.dumps(lists)

