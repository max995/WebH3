###hangman
import nltk
from nltk.corpus import brown
import numpy as np
import string
from collections import Counter
from collections import defaultdict




def hangman(secret_word, guesser, max_mistakes=8, verbose=True, **guesser_args):
    """
        This function plays the hangman game with the provided gusser and returns the number of incorrect guesses.

        secret_word: a string of lower-case alphabetic characters, i.e., the answer to the game
        guesser: a function which guesses the next character at each stage in the game
            The function takes a:
                mask: what is known of the word, as a string with _ denoting an unknown character
                guessed: the set of characters which already been guessed in the game
                guesser_args: additional (optional) keyword arguments, i.e., name=value
        max_mistakes: limit on length of game, in terms of allowed mistakes
        verbose: be chatty vs silent
        guesser_args: keyword arguments to pass directly to the guesser function
    """
    secret_word = secret_word.lower()
    #secret_word=secret_word+"n"
    mask = ['_'] * len(secret_word)
    guessed = set()
    if verbose:
        print("Starting hangman game. Target is", ' '.join(mask), 'length', len(secret_word))

    mistakes = 0
    while mistakes < max_mistakes:
        if verbose:
            print("You have", (max_mistakes - mistakes), "attempts remaining.")
        guess = guesser(mask, guessed, **guesser_args)

        if verbose:
            print('Guess is', guess)
        if guess in guessed:
            if verbose:
                print('Already guessed this before.')
            mistakes += 1
        else:
            guessed.add(guess)
            if guess in secret_word:
                for i, c in enumerate(secret_word):
                    if c == guess:
                        mask[i] = c
                if verbose:
                    print('Good guess:', ' '.join(mask))
            else:
                if verbose:
                    print('Sorry, try again.')
                mistakes += 1

        if '_' not in mask:
            if verbose:
                print('Congratulations, you won.')
            return mistakes

    if verbose:
        print('Out of guesses. The word was', secret_word)
    return mistakes
def human(mask, guessed, **kwargs):
    """
    This is a simple function for manual play.
    """
    print('Enter your guess:')
    return input().lower().strip()
interactive = False
###If you want to play hangman interactively, please set `interactive` to True. When submitting your solution, set to False so we can automatically run the whole notebook using `Run All`.

if interactive:
    hangman('whatever', human, 8, True)


np.random.seed(12345)

# word_set stores all the unique word types in the Brown corpus
word_set = []
# test_set stores 1000 word types for testing
test_set = []
# training_set stores the rest word types for training
training_set = []

###
# Your answer BEGINS HERE
###
texts=[]


for fileid in brown.fileids():
    texts.append(brown.words(fileid))

for doc1 in texts:
    for word in doc1:
        if word.isalpha():
            if word.lower() not in word_set:
                word_set.append(word.lower())

np.random.shuffle(word_set)
test_set=word_set[:1000]
training_set=word_set[1000:]





###
# Your answer ENDS HERE
###

print(len(word_set))
print(len(test_set))
print(len(training_set))

def test_guesser(guesser, test=test_set):
    """
        This function takes a guesser and measures the average number of incorrect guesses made over all the words in the test_set.
    """
    total = 0
    for word in test:
        total += hangman(word, guesser, 26, False)
    return total / float(len(test))





def random_guesser(mask, guessed, **kwargs):
    """
        This function implements a random guesser. It returns the random guess.
    """
    ###
    # Your answer BEGINS HERE
    ###
    s = string.ascii_lowercase
    a = []
    for c in s:
        if c not in list(guessed):
            a.append(c)
    n = np.random.choice(a)
    return n

    ###
    # Your answer ENDS HERE
    ###


# uncomment to run a single hangman game with output shown (useful for debugging)
# hangman(np.random.choice(test_set), random_guesser, 10, True)


result = test_guesser(random_guesser)
print()
print("Average number of incorrect guesses: ", result)




# unigram_counts stores the frequencies of characters over all training words
unigram_counts = Counter()

###
# Your answer BEGINS HERE
###
c_list=[]

for word in training_set:
    for c in word :
        c_list.append(c)

unigram_counts=Counter(c_list)

###
# Your answer ENDS HERE
###

print(unigram_counts)

def unigram_guesser(mask, guessed, unigram_counts=unigram_counts):
    """
        This function implements a unigram guesser. It returns a guess based on the unigram model.
    """
    ###
    # Your answer BEGINS HERE
    ###
    i = len(guessed)
    u_most = unigram_counts.most_common(i + 1)
    m = u_most[-1]
    return m[0]

    ###
    # Your answer ENDS HERE
    ###

#hangman(np.random.choice(test_set), unigram_guesser, 10, True)

result = test_guesser(unigram_guesser)
print()
print("Average number of incorrect guesses: ", result)



# unigram_counts_by_length stores a dictionary, mapping word length to the frequencies of characters of words with that word length
unigram_counts_by_length = defaultdict(Counter)

###
# Your answer BEGINS HERE
###
for word in training_set:
    unigram_counts_by_length[len(word)]=unigram_counts_by_length[len(word)]+Counter(word)


#print(unigram_counts_by_length)

###
# Your answer ENDS HERE
###

lengths = sorted(unigram_counts_by_length.keys())
max_length = lengths[-1] + 1
print(lengths)
print()
print(unigram_counts_by_length)


def unigram_length_guesser(mask, guessed, counts=unigram_counts_by_length):
    """
        This function implements a length-based unigram guesser. It returns a guess based on the length-based unigram model.
    """
    ###
    # Your answer BEGINS HERE
    ###
    i=len(mask)
    m=len(guessed)
    if i in unigram_counts_by_length.keys():
        c1_dict=unigram_counts_by_length[i]
        c1_most=c1_dict.most_common(m+1)
        c1_result=c1_most[-1]
        return c1_result[0]
    else:
        unigram_guesser(mask, guessed, False)

    ###
    # Your answer ENDS HERE
    ###


hangman(np.random.choice(test_set), unigram_length_guesser, 10, True)

result = test_guesser(unigram_length_guesser)
print()
print("Average number of incorrect guesses: ", result)

###
# Your answer BEGINS HERE
###
bigram_counts = Counter() # you will want a different data structure to store the bigram
bigram_counts_list=[]
for word in training_set:
    word ="$"+word
    for i in range(len(word)-1):
        #print((word[i],word[i+1]))
        bigram_counts_list.append((word[i],word[i+1]))

bigram_counts=Counter(bigram_counts_list)

###
# Your answer ENDS HERE
###

def bigram_guesser(mask, guessed, counts=bigram_counts):  # add extra default arguments if needed
    """
        This function implements a bigram guesser. It returns a guess based on the bigram model using linear interpolation.
    """
    ###
    # Your answer BEGINS HERE
    ###
    i=len(mask)


    ###
    # Your answer ENDS HERE
    ###


 hangman(np.random.choice(test_set), bigram_guesser, 10, True)

#result = test_guesser(bigram_guesser)
print()
print("Average number of incorrect guesses: ", result)