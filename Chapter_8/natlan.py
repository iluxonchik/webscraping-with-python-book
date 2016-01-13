from nltk import FreqDist, bigrams, ngrams, pos_tag, word_tokenize, sent_tokenize
from nltk.book import text6

tokens = word_tokenize("Here is some not very interesting text. Let's get its tags!")
print(pos_tag(tokens))

tokens = word_tokenize("The dust was thick so he had to dust.")
print(pos_tag(tokens))

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

sentences = sent_tokenize("Google is one of the best companies in the world. People constantly google stuff.")
nouns = ["NN", "NNS", "NNP", "NNPS"]

for sentence in sentences:
    if "google" in sentence.lower():
        taggedWords = pos_tag(word_tokenize(sentence))
        for word in taggedWords:
            if word[0].lower() == "google" and word[1] in nouns:
                print(sentence)