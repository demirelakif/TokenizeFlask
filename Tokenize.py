import string
from cv2 import threshold
import pandas as pd
import numpy as np           
from ngram import NGram
from typing import List
from jpype import JClass, JString, getDefaultJVMPath, shutdownJVM, startJVM, java

data = pd.read_csv("test.csv",sep=",")
# zemberek-full jar dosyasını C:/Users/kullanici-adi dosya yoluna koyun
ZEMBEREK_PATH = r'C:\Users\Kivanc\zemberek-full.jar' # alttakina göre uyarla
#ZEMBEREK_PATH = r'C:\Users\<your-user-name>\zemberek-full.jar'
startJVM(getDefaultJVMPath(), '-ea', '-Djava.class.path=%s' % (ZEMBEREK_PATH))

TurkishMorphology = JClass('zemberek.morphology.TurkishMorphology')
morphology = TurkishMorphology.createWithDefaults()

def ClearData():
    sentence = "hi; How*, @are^ YOU? wow!!!"
    sentence = sentence.translate(sentence.maketrans('', '', string.punctuation))
    sentence = sentence.lower()
    #print(sentence)
    return sentence


def WordTokenize(sentence):
    word = sentence.split(" ")
    #print(word)

def FindRoot():
        

        # rastgele yazılan kelimeler
        kelimeler = 'kalem ilişkilendiremediklerimiz gözlük gözlem migrsa meleğe duygusuz hiloş gizmo'

        analysis: java.util.ArrayList = (
            morphology.analyzeAndDisambiguate(kelimeler).bestAnalysis()
            )
            
        pos: List[str] = []
        for i, analysis in enumerate(analysis, start=1):
            f'\nAnalysis {i}: {analysis}',
            f'\nPrimary POS {i}: {analysis.getPos()}'
            f'\nPrimary POS (Short Form) {i}: {analysis.getPos().shortForm}'
            
            pos.append(
                f'{str(analysis.getLemmas()[0])}'
                )
        #print(f'\n Kelime Kökleri: {" ".join(pos)}')

        #print("\n çekilen veriii -------------------")
        # boş olan(nan) yerlere "bilinmiyor" yazdırlıyor
        for col in data.columns:
            if data[col].isnull().any():
                data[col] = data[col].fillna("Bilinmiyor")

        def findElements(data):
            result = dict()
            for col in data.columns:
                temp = []
                if col != "Id":
                    for i in data[col]:
                        #print(i)
                        if i != "Bilinmiyor":
                            temp.append(i)
                    result[col] = temp
            return result


        myDic = findElements(data)

        #print(myDic["Key"])

        allWords = " ".join(myDic["Key"])
        allCatagories = " ".join(myDic["Key"])

        #print(allWords)

        #print("\n çekilen verilerin zemberekten geçmiş hali -------------- \n")

        analysis: java.util.ArrayList = (
            morphology.analyzeAndDisambiguate(allWords).bestAnalysis()
            )
            
        pos: List[str] = []
        for i, analysis in enumerate(analysis, start=1):
            f'\nAnalysis {i}: {analysis}',
            f'\nPrimary POS {i}: {analysis.getPos()}'
            f'\nPrimary POS (Short Form) {i}: {analysis.getPos().shortForm}'
            
            pos.append(
                f'{str(analysis.getLemmas()[0])}'
                )
        #print(f'\n Kelime Kökleri: {" ".join(pos)}')
        WordArray = " ".join(pos)
        return WordArray
        

#prog_dilleri = ["migros", "bim", "metro", "a101","ruby", "java", "haskell", "erlang"]



def aramaYap(v,ara):
        # for i in v.search(ara, threshold=0.1):
        #     print("Önerilen:", i[0], "-- Yakınlık:", i[1], "\n")
        

        value = v.search(ara,threshold = 0.1)
        return value





   
def start (value):
    WordTokenize(ClearData())
    prog_dilleri =  FindRoot().split()
    v = NGram(prog_dilleri)
    return aramaYap(v,value)



#import nltk
#from nltk.tokenize import word_tokenize
# word_tokenize("hi; How*, @are^ YOU? wow!!!")