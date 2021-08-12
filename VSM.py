import os
import nltk
import pathlib
import json
from tkinter import *
from collections import OrderedDict
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
import math
import numpy as np

def pre_processing(path,id):         #preprocessing each document and creating indexes of each document
    contractions = {
    "ain't": "am not / are not",
    "aren't": "are not / am not",
    "can't": "cannot",
    "can't've": "cannot have",
    "'cause": "because",
    "could've": "could have",
    "couldn't": "could not",
    "couldn't've": "could not have",
    "didn't": "did not",
    "doesn't": "does not",
    "don't": "do not",
    "hadn't": "had not",
    "hadn't've": "had not have",
    "hasn't": "has not",
    "haven't": "have not",
    "he'd": "he had / he would",
    "he'd've": "he would have",
    "he'll": "he shall / he will",
    "he'll've": "he shall have / he will have",
    "he's": "he has / he is",
    "how'd": "how did",
    "how'd'y": "how do you",
    "how'll": "how will",
    "how's": "how has / how is",
    "i'd": "I had / I would",
    "i'd've": "I would have",
    "i'll": "I shall / I will",
    "i'll've": "I shall have / I will have",
    "i'm": "I am",
    "i've": "I have",
    "isn't": "is not",
    "it'd": "it had / it would",
    "it'd've": "it would have",
    "it'll": "it shall / it will",
    "it'll've": "it shall have / it will have",
    "it's": "it has / it is",
    "let's": "let us",
    "ma'am": "madam",
    "mayn't": "may not",
    "might've": "might have",
    "mightn't": "might not",
    "mightn't've": "might not have",
    "must've": "must have",
    "mustn't": "must not",
    "mustn't've": "must not have",
    "needn't": "need not",
    "needn't've": "need not have",
    "o'clock": "of the clock",
    "oughtn't": "ought not",
    "oughtn't've": "ought not have",
    "shan't": "shall not",
    "sha'n't": "shall not",
    "shan't've": "shall not have",
    "she'd": "she had / she would",
    "she'd've": "she would have",
    "she'll": "she shall / she will",
    "she'll've": "she shall have / she will have",
    "she's": "she has / she is",
    "should've": "should have",
    "shouldn't": "should not",
    "shouldn't've": "should not have",
    "so've": "so have",
    "so's": "so as / so is",
    "that'd": "that would / that had",
    "that'd've": "that would have",
    "that's": "that has / that is",
    "there'd": "there had / there would",
    "there'd've": "there would have",
    "there's": "there has / there is",
    "they'd": "they had / they would",
    "they'd've": "they would have",
    "they'll": "they shall / they will",
    "they'll've": "they shall have / they will have",
    "they're": "they are",
    "they've": "they have",
    "to've": "to have",
    "wasn't": "was not",
    "we'd": "we had / we would",
    "we'd've": "we would have",
    "we'll": "we will",
    "we'll've": "we will have",
    "we're": "we are",
    "we've": "we have",
    "weren't": "were not",
    "what'll": "what shall / what will",
    "what'll've": "what shall have / what will have",
    "what're": "what are",
    "what's": "what has / what is",
    "what've": "what have",
    "when's": "when has / when is",
    "when've": "when have",
    "where'd": "where did",
    "where's": "where has / where is",
    "where've": "where have",
    "who'll": "who shall / who will",
    "who'll've": "who shall have / who will have",
    "who's": "who has / who is",
    "who've": "who have",
    "why's": "why has / why is",
    "why've": "why have",
    "will've": "will have",
    "won't": "will not",
    "won't've": "will not have",
    "would've": "would have",
    "wouldn't": "would not",
    "wouldn't've": "would not have",
    "y'all": "you all",
    "y'all'd": "you all would",
    "y'all'd've": "you all would have",
    "y'all're": "you all are",
    "y'all've": "you all have",
    "you'd": "you had / you would",
    "you'd've": "you would have",
    "you'll": "you shall / you will",
    "you'll've": "you shall have / you will have",
    "you're": "you are",
    "you've": "you have"
    }
    file_content=""

    with open(path, 'r',encoding='utf-8') as f:    #reading the documents
        file_content=f.read()
    f.close()
    # print(file_content)

    words = []
    l=file_content.split()
    for word in l:                                        #removing contractions
        if word in contractions:
            words.append(contractions[word])
        else:
            words.append(word)

    file_content = ""
    file_content = ' '.join(words)

    new = ""
    punctuations = '''!()[]{};:'"\,<‘>./?@#$%^&*_~“”’'''

    file_content.replace("\n", " ")

    for w in file_content:                                  #removing punctuatations and stemming
        if w not in punctuations:
            new = new + w

    new = new.replace("—", "")
    new=new.replace("-","")

    new = new.lower()

    words_dict = nltk.word_tokenize(new)
    ps= PorterStemmer()
    wd=[]
    for i in words_dict:        
        i=ps.stem(i)
        wd.append(i)

    words_dict1 = list(dict.fromkeys(wd))

    stopwords = ["am", "is", "the", "of", "all", "and", "to", "can", "be", "as", "once", "for", "at", "a", "are",
                         "has", "have", "had", "up", "his", "her", "in", "on", "no", "we", "do"]

    context = dict()
    idf_index=dict()
    N=50
    for i in wd:       #removing stopwords and creating index of the given document
        if i not in stopwords:
            if i in context:
                context[i][id]=context[i][id]+1
            else:
                context[i]=dict()
                context[i][id]=1
    
    return context             #returning indexe

def indexing(h1,h2):            #merging the indexes of two document
    for i in h1:
        if i in h2:
            h2[i].update(h1[i])
        else:
            h2[i]=h1[i]
    return h2                               #returning the combined dictionary

def merge_inverted(dict1,dict2):   #merging the indexes of two document
    for i in dict1.keys():
        if i in dict2:
            dict2[i]=dict1[i]+dict2[i]
        else:
            dict2[i]=dict1[i]
    return dict2    #returning the combined index

def create_indexes():    #creating the both complete indexes of all the documents 
    ps=PorterStemmer()   
    dataset=os.getcwd()
    dataset=dataset+'\ShortStories'
    idf_index=dict()
    inverted_index=dict()
    N=50
    for txt_file in os.listdir(dataset):    #traversing the given path
        doc_id=int(txt_file.split('.')[0])
        inverted=pre_processing(os.path.join(dataset,txt_file),str(doc_id))
        inverted_index=indexing(inverted_index,inverted)
    for word in inverted_index:
        # idf_index[word]=round(math.log10(N/len(inverted_index[word].keys())),5)
        idf_index[word]=round(math.log10(len(inverted_index[word].keys()))/N,3)
    return inverted_index,idf_index   #returning both indexes
def cosine_sim(q_vect,doc_vect,alpha):
    dot=np.dot(q_vect,doc_vect)
    similar=round(dot/(np.linalg.norm(q_vect)*np.linalg.norm(doc_vect)),3)
    if similar>=float(alpha):
        return similar
    else:
        return -1



def main1(Query,alpha,root,l1):
    file1=os.getcwd()+'\doctf_index.json'
    file2=os.getcwd()+'\idf_index.json'
    tf=dict()
    idf=dict()
    if not os.path.exists(file2):   #if index are not created it will create and save the model
        tf,idf=create_indexes()
        json_object_tf = json.dumps(tf)
        json_object_idf = json.dumps(idf)
        with open("doctf_index.json", "w") as outfile:
            outfile.write(json_object_tf)

        with open("idf_index.json", "w") as outf:
            outf.write(json_object_idf)
    else:           #or else it will only load the json object if file exists
        with open('doctf_index.json', 'r') as openfile:
            tf = json.load(openfile)
        with open('idf_index.json', 'r') as openfile:
            idf = json.load(openfile)

    words_len=len(tf)
    print(words_len)
    vectors=dict()
    for i in range(1,51):
        vectors[str(i)]= np.zeros(words_len,dtype=float)
        count=0
        for word in tf:
            if str(i) in tf[word]:
                vectors[str(i)][count]=float(tf[word][str(i)])*float(idf[word])
            count+=1
    query=Query
    alpha1=0.005
    if alpha!="":
        alpha1=float(alpha)
    q1=nltk.word_tokenize(query)
    ps=PorterStemmer()
    q_final=dict()
    for k in q1:
        if k not in q_final:
            k=ps.stem(k)
            q_final[k]=1
        else:
            q_final[k]+=1
    q_vect=np.zeros(words_len,dtype=float)
    counter=0
    for w in idf:
        if w in q_final:
            q_vect[counter]=q_final[w]
        counter+=1
    result=[]
    for docs in vectors:
        sim=cosine_sim(q_vect,vectors[docs],alpha1)
        if sim!=-1:
            result.append((docs,sim))
    result.sort(key=lambda x: x[1],reverse=True)
    document_count=len(result)
    print(result)


    a='Result Set of query: '+Query
    Label(root,text=a,font=('Helvetica',25,'bold'),fg='blue').pack(pady=5,padx=5)

    fi=' '.join(str([x[0] for x in result]))
    l1.delete("1.0",END)
    l1.insert(END,fi)
    l1.insert(END,"\nTotal number of Document retrieved: "+str(document_count))
    result=[]


