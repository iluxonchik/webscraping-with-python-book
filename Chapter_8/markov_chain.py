from urllib.request import urlopen
from random import randint

PONCTUATION = [',', '.', ';', ':']


def word_list_sum(word_list):
    sum = 0
    for word, value in word_list.items():
        sum += value
    return sum

def retrieve_random_word(word_list):
    rand_index = randint(1, word_list_sum(word_list))
    for word, value in word_list.items():
        rand_index -= value
        if rand_index <= 0: # words with higher frequency will hit this with higher probability
            return word

def build_word_dict(text):
    # Remove newlines and quotes
    text = text.replace('\n', ' ')
    text = text.replace('\"', '')

    # Treat ponctuation as words, so that it gets included in the Markov Chain
    for symbol in PONCTUATION:
        text = text.replace(symbol, ' ' + symbol + ' ')
        words = text.split(' ')
        # Remove empty words
        words = [word for word in words if word != '']

        word_dict = {}
        for i in range(1, len(words)):
            if words[i-1] not in word_dict:
                # Create a new dictionary for this word
                word_dict[words[i-1]] = {}
            if words[i] not in word_dict[words[i-1]]:
                word_dict[words[i-1]][words[i]] = 0
            word_dict[words[i-1]][words[i]] += 1
    return word_dict

text = str(urlopen('http://pythonscraping.com/files/inaugurationSpeech.txt').read(), 'utf-8')
word_dict = build_word_dict(text)

# Generate a Markov chain of lenght 100
length = 100
chain = ''
current_word = 'I'
for i in range(length):
    if current_word in PONCTUATION:
        chain += current_word
    else:
        chain += ' ' + current_word
    
    current_word = retrieve_random_word(word_dict[current_word])
print(chain)