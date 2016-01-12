from nltk import word_tokenize
from nltk import Text
from nltk import FreqDist, bigrams, ngrams
from nltk.book import text6

tokens = word_tokenize("Here is some not very interesting text")
text = Text(tokens)

fdist = FreqDist(text6)
print(fdist.most_common(10))

bigrams = bigrams(text6)
bigramDist = FreqDist(bigrams)
print(bigramDist[("Sir", "Robin")])

fourgrams = ngrams(text6, 4)
fourgramsDist = FreqDist(fourgrams)
print(fourgramsDist[("father", "smelt", "of", "elderberries")])

for fourgram in fourgrams:
    if fourgram[0] == "coconut":
        print(fourgram)