#python3 endemic.py &

import sys, random
import os
import nltk, re, string, collections
from nltk.util import ngrams # function for making ngrams

if __name__ == '__main__':
    folder_path= "../tokenized/"
    arr = os.listdir(folder_path)
    total_grams= 0;
    endemic_grams = 0;
    read_size= 512*1024
    for i in range (0,len(arr)):
        file_path =folder_path+arr[i] 
        output_file = open( arr[i]+str("_zipf.txt"), 'w')
        unique_grams_partial= collections.Counter();
        text= ""
        with open(file_path, "r", encoding="utf8", errors="surrogateescape") as fh:
            lines = fh.read().splitlines(1)
            #text=fh.readlines()[0:100] #put here the interval you want
            while len(text.encode('utf-8')) < read_size:
                    text = text +  random.choice(lines)

            #output_file.write(text)


            
            # first get individual words
            tokenized = text.split()

            # and get a list of all the n-grams
            xgrams = ngrams(tokenized, 1)
            # get the frequency of each bigram in our corpus
            xgramFreq=collections.Counter(xgrams)
            xgramFreq = dict(xgramFreq.most_common())
            #xgramFreq = sorted(xgramFreq.items(), key=lambda pair: pair[1], reverse=True)
            
            for item in xgramFreq:
                output_file.write( str(xgramFreq[item]) + ",")
  
                
            output_file.close();    
        output_file.close();      



        