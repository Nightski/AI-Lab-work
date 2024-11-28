import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

text = "This is an example of sentence removal of stopwords."
stop = word_tokenize(text)
rem = set(stopwords.words('english'))
ans = " ".join(c for c in stop if c.lower() not in rem)
print(stop)
print()
print(ans)