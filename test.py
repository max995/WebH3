from nltk.corpus import brown
import numpy as np
import string
from collections import defaultdict
from collections import Counter

unigram_counts_by_length = defaultdict(Counter)

print(type(unigram_counts_by_length))