import numpy as np
import re
from nltk.tokenize import word_tokenize, sent_tokenize

file = open("ArabicWords.txt", mode='r')
file2 = open("EnglishWords.txt", mode='r')

fileLines = file.readlines()
file2Lines = file2.readlines()

ArabicLinesArray = np.array(fileLines)
EnglishLinesArray = np.array(file2Lines)

EnglishLinesArray.sort()

stringTest = "la2 ya7beby n3m 2aa 23423"

RE_For_Arabic = r"[ء-ي]"
RE_For_English = r"[A-Za-z]+"
RE_For_Franco = r"[A-Za-z]+\d[A-Za-z]+|[A-Za-z]+\d|\d[A-Za-z]+"

print(re.findall(RE_For_Franco, stringTest))




if(len(re.findall(RE_For_English, stringTest)) != 0):
    if (len(re.findall(RE_For_Franco, stringTest)) != 0):
        print("Franco")
    else:
        print("English")
elif(len(re.findall(RE_For_Arabic, stringTest)) != 0):
    print("Arabic")
else:
    print("Language is unknown")


re.findall(RE_For_English, stringTest)