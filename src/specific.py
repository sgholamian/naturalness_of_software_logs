import sys
import os
import nltk, re, string, collections
from nltk.util import ngrams # function for making ngrams
import math
from itertools import combinations 

if __name__ == '__main__':

    num_files= 8
    arr = os.listdir("../tokenized/")
    total_grams= 0;
    file_size= 1024*100
    set_size = len(arr)
    comb = combinations(arr, num_files) 
    gram_size = 5
    fh=  [None] *num_files; text = [None] *num_files;xgramFreq= [None] *num_files; tokenized = [None] *num_files
    xgrams= [None] *num_files;
    for item in comb: 
        #print(item)  
        for i in range(0, num_files):
            fh [i] = open("../tokenized/"+str(item[i]), "r");
            text[i] = fh[i].read(file_size);
            tokenized[i] = text[i].split()
            xgrams[i] = ngrams(tokenized[i], gram_size)
            xgramFreq[i] = collections.Counter(xgrams[i])
        total_list=collections.Counter()
        for i in range (0, num_files):
            for item in xgramFreq[i]:
                if item in total_list:
                    #print("added to toal list: ", item, total_list[item])
                    total_list[item] = total_list[item] + xgramFreq[i][item]
                else:
                    total_list[item] = xgramFreq[i][item]
                

        #print(total_list)
		
        count_print=0
        for item in total_list:
            token_entropy =0;
            for i in range(0,num_files):
                if item in xgramFreq[i]:
                    freq= float(xgramFreq[i][item])/ total_list[item]
                    #print("freq is: " , xgramFreq[i][item], total_list[item] )
                    if(freq < 1):
                        token_entropy = token_entropy + freq * math.log(freq, 2)
            token_entropy= -token_entropy    
            if(token_entropy>0):
                count_print = count_print +1
                print(token_entropy, end=',')
                #if count_print> 10:
                #    break;
            
        
        
    print("")

    sys.exit(0)            
            
            
        

    
  

    
    
    
    for i in range (0,(len(arr)-1)):
        #print("file name is:" + arr[i])
        #print("calculating the unique tokens in file: ", arr[i])
        file_path ="../tokenized/"+arr[i] 
        total_count_gram = collections.Counter();
            
        with open(file_path, "r", encoding="utf8", errors="surrogateescape") as fh:
            text = fh.read(1024);
            #text=fh.readlines()[0:100] #put here the interval you want
            
            # first get individual words
            tokenized = text.split()

            # and get a list of all the bi-grams
            xgrams = ngrams(tokenized, gram_size)
            # get the frequency of each bigram in our corpus
            xgramFreq=collections.Counter()
            xgramFreq = collections.Counter(xgrams)
            #print ("number of ngrams are: ", len(xgramFreq))
            if i==0:
                total_grams = total_grams + len(xgramFreq)        
            
            for j in range (i+1, len(arr)):
                if j != i:
                    file_path_2 = "../tokenized/"+arr[j] 
                    with open(file_path_2, "r", encoding="utf8", errors="surrogateescape") as fh2:
                        text2 = fh2.read(1024);
                        # first get individual words
                        tokenized2 = text2.split()
                        xgrams2=[]
                        # and get a list of all the bi-grams
                        xgrams2 = ngrams(tokenized2, gram_size)
                        # get the frequency of each bigram in our corpus
                        xgramFreq2 = collections.Counter(xgrams2)
                        if i==0:
                            total_grams = total_grams + len(xgramFreq2) 
                        #print("file i is: ", arr[i], " and file j is: ", arr[j])
                        ent = 0.0                        
                        for item in xgramFreq.keys():
                            if item in xgramFreq2.keys():
                                freq_total = (xgramFreq2[item] + xgramFreq[item]); 
                                
                                ent = ent + freq * math.log(freq, 2)
                                #print(freq)
                        ent = -ent                        
                                
                                #print(" added item to the list: " , item)
                            #else: 
                                #print ("item is: ", item, " freq 1 is: ", xgramFreq[item], " freq 2 is: ", xgramFreq2[item]);
                        
                        #    if freq > 0:
                        #        ent = ent + freq * math.log(freq, 2)
                        xgramFreq = collections.Counter()
                        xgramFreq = unique_grams_partial
                        unique_grams_partial = collections.Counter()
                        #print("new set of endemic size is: " , len(xgramFreq))
        
        freq_2plus=0
        for item in xgramFreq:
            if xgramFreq[item]>1:
                freq_2plus= freq_2plus+1;
            
        print(arr[i] , len(xgramFreq) , freq_2plus)



        