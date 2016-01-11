from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict
import re, string, operator

def clean_input(input):
    input = re.sub('\n+', ' ', input) # substitute single or multiple consecutive '\n' by a space
    input = re.sub(' +', ' ', input)
    input = re.sub('\[[0-9]*\]', '', input) # remove numbers enclosed by brackets
    input = bytes(input, 'UTF-8')
    input = input.decode('ascii', 'ignore')
    input = input.lower()
    clean_input = []

    input = input.split(' ')
    for item in input:
        item = item.strip(string.punctuation) # strip ponctuation from left and right of the string
        if len(item) > 1 or (item.lower() in ('a', 'i')):
            clean_input.append(item)

    return clean_input

def ngrams(input, n):
    input = clean_input(input)
    output = {}
    for i in range(len(input)- n + 1):
        ngram_temp = ' '.join(input[i:i+n]) # transform list to string
        if ngram_temp not in output:
            output[ngram_temp] = 1
        else:
            output[ngram_temp] += 1
    return output

content = str(urlopen('http://pythonscraping.com/files/inaugurationSpeech.txt').read())
ngrams = ngrams(content, 2)
sorted_ngrams = sorted(ngrams.items(), key=operator.itemgetter(1), reverse=True)
print(sorted_ngrams)