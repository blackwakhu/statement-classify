from textblob.classifiers import NaiveBayesClassifier 

with open('words.csv', 'r') as word:
	cl = NaiveBayesClassifier(word, format="csv")

def classifiable(statement):
	return cl.classify(statement)