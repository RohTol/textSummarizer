#https://www.geeksforgeeks.org/python-text-summarizer/
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize 
import nltk
nltk.download('stopwords')
nltk.download('punkt')

text = input("input paragraph here:")

stopWords = set(stopwords.words("english")) 
words = word_tokenize(text) 
freqTable = dict() 
for word in words:
    word = word.lower()
    if word in stopWords:
        continue
    if word in freqTable:
        freqTable[word] += 1
    else:
        freqTable[word] = 1


sentences =  sent_tokenize(text)
sentenceValue = dict()
for sentence in sentences:
    for word, freq in freqTable.items():
        if word in sentence.lower():
            if sentence in sentenceValue:
                sentenceValue[sentence] += freq
            else:
                sentenceValue[sentence] = freq

sumValues = 0
for sentence in sentenceValue:
    sumValues += sentenceValue[sentence]

average = int(sumValues / len(sentenceValue))

summary = ''
for sentence in sentences:
    if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
        summary += " " + sentence
#print new lines
print("\n\n\nSummary:" )
print(summary)
