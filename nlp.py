import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.classify import PositiveNaiveBayesClassifier

# # nltk.download() to download pakages required for 
# data ="hello world how `are'  you.i am fine how do you do"
# words = word_tokenize(data) #Object created in the name of word
# # print(words)
# stopwords = set(stopwords.words('english'))
# wordsFilter = []

# for w in words:
#     if w not in wordsFilter:
#         wordsFilter.append(w)

# print(wordsFilter)
# sentence = "hey john.danaries has come for you. go and see her."
# phrase =sent_tokenize(sentence)
# print(phrase)

# NLTK STEMMING
# ps = PorterStemmer()
# word_1 = ["gaming","games","gaming","seeing"]
# sentence_1 = "seeing sees saying says told lies fathers"
# sentence_a = word_tokenize(sentence_1)

# for k in sentence_a:
#     print("stemmed word is : {}".format(ps.stem(k)))


sports_sentences = [ 'The team dominated the game',
                      'They lost the ball',
                      'The game was intense',
                      'The goalkeeper catched the ball',
                      'The other team controlled the ball' ]

various_sentences = [ 'The President did not comment',
                       'I lost the keys',
                       'The team won the game',
                       'Sara has two kids',
                       'The ball went off the court',
                       'They had the ball for the whole game',
                       'The show is over' ]
def features(sentence):
     words = sentence.lower().split()
     return dict(('contains(%s)' % w, True) for w in words)

positive_featuresets = pip install numpymap(features, sports_sentences)
unlabeled_featuresets = map(features, various_sentences)
classifier = PositiveNaiveBayesClassifier.train(positive_featuresets, unlabeled_featuresets)

print(classifier.classify(features('The show is over')))



