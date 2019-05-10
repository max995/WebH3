import string
from collections import Counter

from H3 import unigram_counts

bigram_counts = {}  # you will want a different data structure to store the bigram
bigram_linear={}
a = list(string.ascii_lowercase)

# for c in a:
#     print(c)
#     bigram_counts[c]=Counter()
#     bigram_linear[c]=Counter()
print(a)
bigram_counts['$']=Counter()
bigram_linear['$']=Counter()
bi_lambdas=8
sumall=sum(unigram_counts.values())
prin
#print(sumall)
