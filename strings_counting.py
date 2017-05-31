# -*- coding: utf-8 -*-
"""
Two alternatives ways to count words/strings

"""

################## Solution 1
unwanted_chars = ".,-_()/\#%!"
    
opec = open("C:/Users/bre49823/Desktop/opec_newsletter.txt", encoding = "utf8").read()
opec2 = opec.replace("\n", " ")
opec3 = opec2.strip(unwanted_chars)
opec3 = opec3.lower()
opec3 = opec3.split(" ")

opec_words = ['aa', 'bb', 'ff', 'ff', 'aa']

len(opec_words)

def wordListToFreqDict(words):
    wordfreq = [words.count(p) for p in words]
    return dict(zip(words, wordfreq))

words_frequency = wordListToFreqDict(opec_words)

sorted(words_frequency.values())


################## Solution 2
############################## !!!! NEEDS MORE WORK !!!!!

import sys

filename = sys.argv[1]
fp = open(filename)
data = fp.read()
words = data.split()
fp.close()

unwanted_chars = ".,-_ (and so on)"
wordfreq = {}
for raw_word in words:
    word = raw_word.strip(unwanted_chars)
    if word not in wordfreq:
        wordfreq[word] = 0 
    wordfreq[word] += 1