# Code to count repeat words in a file #
# Code assumes all punctuation as part of the word itself 
# Each tweet only contains lowercase letters, numbers, and ASCII characters like ':', '@', and '#'.
# A word is defined as anything separated by whitespace. 

with open("Tweet_input/tweets.txt", 'r') as f:
    testString = f.read()
dic = {}
sorted_dic ={}
words = testString.split()
for raw_word in words:
    word = raw_word.lower()
    if word in dic:
        dic[word] += 1
    else:
        dic[word] = 1
        
with open("Tweet_output/ft1.txt", 'w') as g:
    
    for word in sorted(dic.items()):
        s = str(word)
        g.write(s)
        g.write('\n')
        print (s) 
        
    

# Code to count median unique number of words per line #
# Inbuilt command in python "collections.Counter" is used.
# Command "collections.Counter" does not consider all punchuations as par of a word. 
# Therefore the command results in larger number of words per line.

import collections
import re
import statistics

list = []      # list array stores the number of unique #

with open("Tweet_output/ft2.txt", 'w') as h:

    for line in open("Tweet_input/tweets.txt",'r').readlines():
        words = re.split("\W+",line.lower())
        words_count = collections.Counter(words) #Count the occurrence of each word
        Unique_words = len(words_count)
        list.append(Unique_words)
        t = str(statistics.median(map(float, list)))
        h.write(t)
        h.write('\n')
        print ( '\nMedian of unique words per line:', t)

    
