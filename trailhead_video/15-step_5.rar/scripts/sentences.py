import nltk.data
import re
import string

nltk.download('punkt')
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

with open('poem.txt') as f:
    data = f.read()
    data = data.replace('\n', ' ')
    data = re.sub('\d', '', data)
    sentences = tokenizer.tokenize(data)
    for i in range(len(sentences)):
        sentences[i] = sentences[i].translate(str.maketrans('', '', string.punctuation))
        sentences[i] = sentences[i].replace(' ', '').upper()
        print(sentences[i])
