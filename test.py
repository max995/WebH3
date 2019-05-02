from nltk.corpus import brown
import numpy as np
import string

g={'f'}
s = string.ascii_lowercase
a=[]
for c in s :
    if c not in list(g):
        a.append(c)

n=np.random.choice(a,replace=False)
print(n)

