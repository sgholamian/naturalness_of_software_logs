#python3 endemic.py &

import sys
import os
import nltk, re, string, collections
from nltk.util import ngrams # function for making ngrams

if __name__ == '__main__':
    gram_size= 10
    output_file = open( str(gram_size)+str("_endemic.txt"), 'w')
    folder_path= "../tokenized/"
    arr = os.listdir(folder_path)
    total_grams= dict();
    endemic_grams = 0;
    print_size=100;
    read_size=1024*1024*10
    for i in range (0,len(arr)):
        #print("file name is:" + arr[i])
        #print("calculating the unique tokens in file: ", arr[i])
        file_path =folder_path+arr[i] 
        unique_grams_partial= collections.Counter();
        with open(file_path, "r", encoding="utf8", errors="surrogateescape") as fh:
            text = fh.read(read_size);
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
                total_grams = dict(xgramFreq)      
            
            for j in range (0, len(arr)):
                if j != i:
                    file_path_2 = folder_path+arr[j] 
                    with open(file_path_2, "r", encoding="utf8", errors="surrogateescape") as fh2:
                        text2 = fh2.read(read_size);
                        # first get individual words
                        tokenized2 = text2.split()
                        xgrams2=[]
                        # and get a list of all the bi-grams
                        xgrams2 = ngrams(tokenized2, gram_size)
                        # get the frequency of each bigram in our corpus
                        xgramFreq2 = collections.Counter(xgrams2)
                        if i==0:
                            for item in xgramFreq2:
                                if item in total_grams:
                                    total_grams[item] = total_grams[item] + xgramFreq2[item]
                                else:
                                    total_grams [item] = xgramFreq2[item]
                        if len(total_grams) > print_size:
                                print("total gram is:" ,len(total_grams), file_path, file_path_2)
                                print_size= len(total_grams)
                                    
                                
                                   
                                    

                        #print("file i is: ", arr[i], " and file j is: ", arr[j]) 
                        # for item in xgramFreq.keys():
                            # if item not in xgramFreq2.keys():
                                # unique_grams_partial [item] = xgramFreq[item]; 
                                # #print(" added item to the list: " , item)
                            # #else: 
                                #print ("item is: ", item, " freq 1 is: ", xgramFreq[item], " freq 2 is: ", xgramFreq2[item]);
                        xgramFreq_temp = dict(xgramFreq)
                        for item in xgramFreq.keys():
                            if item in xgramFreq2.keys():
                                del xgramFreq_temp[item];
                                    #unique_grams_partial [item] = xgramFreq[item]; 
                                #print(" added unique item to the list: " , item)
                            #else: 
                            #    print ("item is: ", item, " freq 1 is: ", xgramFreq[item], " freq 2 is: ", xgramFreq2[item]);
                        xgramFreq=[]
                        xgramFreq=dict(xgramFreq_temp)
                        
                        #xgramFreq = collections.Counter()
                        #xgramFreq = unique_grams_partial
                        #unique_grams_partial = collections.Counter()
            for item in xgramFreq:
                unique_grams_partial[item] = xgramFreq[item] 
                        #print("new set of endemic size is: " , len(xgramFreq))
        
        
        total_grams = collections.Counter(total_grams)
        
        if i==0:
            freq_2plus=0
            for item in total_grams:
                if total_grams[item]>1:
                    freq_2plus= freq_2plus+1;
            output_file.write("for gram size: " + str(gram_size) + " total grams are: " + str( len(total_grams)) +" " + str(freq_2plus) + "\n" )
            print("for gram size: " + str(gram_size) + " total grams are: " + str( len(total_grams)) +" freq of 2 or more: " + str(freq_2plus))
        freq_2plus=0
        for item in unique_grams_partial:
            if unique_grams_partial[item]>1:
                freq_2plus= freq_2plus+1;
            
        #print(gram_size, arr[i] , len(xgramFreq) , freq_2plus)
        output_file.write(str(gram_size)+ " "  + str(len(unique_grams_partial))+ " " + str(freq_2plus)+ "\n")
        print(str(gram_size)+ " " + str(arr[i]) + " " + str(len(unique_grams_partial))+ " " + str(freq_2plus))
    output_file.close();    



        