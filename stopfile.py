import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def remove(path,opath):
    stoper = set(stopwords.words('english'))

    try:
        with open(path, 'r') as file:
            text = file.read()
        words = word_tokenize(text)
        filt = [word for word in words if word.lower() not in stoper]
        flitered = " ".join(filt)

        with open(opath, 'w') as op:
            op.write(flitered)
        print("Done")
    except FileNotFoundError:
        print("No file found")




path = 'input.txt'
opath = 'output.txt'
remove(path, opath)