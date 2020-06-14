import nltk
import string
import collections
from nltk.util import ngrams
import sys
import rolling_hash


n=int(sys.argv[1])


with open("1000 Malicious Exe Samples/TextDump/10-27-18-839 1 (10).txt",'r') as f:
	text=f.read()

#print(text)

token=text.split()

ngram=list(ngrams(token,n))
#print (trigram)


ngramFreq = collections.Counter(ngram)


print(ngramFreq.most_common(10))
	