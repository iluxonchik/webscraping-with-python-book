from urllib.request import urlopen
from bs4 import BeautifulSoup
import re, string

def clean_input(input):
    input = re.sub('\n+', ' ', input) # substitute single or multiple consecutive '\n' by a space
    input = re.sub(' +', ' ', input)
    input = re.sub('\[[0-9]*\]', '', input) # remove numbers enclosed by brackets
    input = bytes(input, 'UTF-8')
    input = input.decode('ascii', 'ignore')
    clean_input = []

    input = input.split(' ')
    for item in input:
        item = item.strip(string.punctuation) # strip ponctuation from left and right of the string
        if len(item) > 1 or (item.lower() in ('a', 'i')):
            clean_input.append(item)

    return clean_input

def ngrams(input, n):
    input = clean_input(input)
    output = []
    for i in range(len(input)-n+1):
        output.append(input[i:i+n])
    return output

html = urlopen('http://en.wikipedia.org/wiki/Python_(programming_language)')
bsObj = BeautifulSoup(html, 'html.parser')
content = bsObj.find('div', {'id':'mw-content-text'}).get_text()
ngrams = ngrams(content, 2)
print(ngrams)
print("2-gram count is " + str(len(ngrams)))