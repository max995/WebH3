###hangman
import nltk
from nltk.corpus import brown
import numpy as np







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
data_raw = brown.paras()
data1= brown.words(data_raw)###???
data=[]
for doc1 in data_raw:
    doc=[]
    for para1 in doc1:
        for word in para1:
            if word.isalpha():
                doc.append(word.lower())
    data.append(doc)


###
# Your answer ENDS HERE
###

print(len(word_set))
print(len(test_set))
print(len(training_set))