 # -*- coding: utf-8 -*-
"""
Created on Wed May 23 14:05:55 2018

@author: SilverDoe
"""


#=========================  Solution using levenshtein  =======================

import re
import zipfile
import numpy as np
try:
    from xml.etree.cElementTree import XML # cElementTree is implemented in C. Much faster than python implementation
except ImportError:
    print('exception occured : Unable to use c implementation of ElementTree. Trying native implementation!!! ')
    from xml.etree.ElementTree import XML # ElementTree is implemented in Python


class FilterPyDocx:
    
    WORD_NAMESPACE = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
    PARA = WORD_NAMESPACE + 'p'
    TEXT = WORD_NAMESPACE + 't'
    paragraphs = []
    data = ''
    words = []
    filteredData = ''
    sentenceList = []
    
    
    def __init__(self,filePath):
        
        document = zipfile.ZipFile(filePath)
        xml_content = document.read('word/document.xml')
        document.close()
        tree = XML(xml_content)
        
        for paragraph in tree.getiterator(self.PARA):
            texts = [node.text for node in paragraph.getiterator(self.TEXT) if node.text]
            if texts:
                self.paragraphs.append(''.join(texts))
                sentenceEnders = re.compile('[.!?][\s]{1,2}(?=[A-Z])')
                self.sentenceList = self.sentenceList + sentenceEnders.split(''.join(texts))
                      
        self.data = '\n\n'.join(self.paragraphs)
        self.words = re.findall(r"[\w']+", self.data)
        self.filteredData = ' '.join(self.words)
        
    def getParagraphs(self):
        return self.paragraphs
        
    def getFilteredData(self):
        return self.filteredData
    
    def getWordList(self):
        return self.words
    
    def getSentenceList(self):
        return self.sentenceList
    
    
    
    
class SimilarityFinder:
    
    def levenshtein(self,source, target):
        if len(source) < len(target):
            return self.levenshtein(target, source)

        # So now we have len(source) >= len(target).
        if len(target) == 0:
            return len(source)

        # We call tuple() to force strings to be used as sequences
        # ('c', 'a', 't', 's') - numpy uses them as values by default.
        source = np.array(tuple(source))
        target = np.array(tuple(target))

        # We use a dynamic programming algorithm, but with the
        # added optimization that we only need the last two rows
        # of the matrix.
        previous_row = np.arange(target.size + 1)
        for s in source:
            # Insertion (target grows longer than source):
            current_row = previous_row + 1

            # Substitution or matching:
            # Target and source items are aligned, and either
            # are different (cost of 1), or are the same (cost of 0).
            current_row[1:] = np.minimum(
                    current_row[1:],
                    np.add(previous_row[:-1], target != s))

            # Deletion (target grows shorter than source):
            current_row[1:] = np.minimum(
                    current_row[1:],
                    current_row[0:-1] + 1)

            previous_row = current_row

        return previous_row[-1]
    
    
        
    
obj = FilterPyDocx('E:\\Documents\\PythonProjects\\1_Basics\\DataForFiles\\protest.docx')
slist1 = obj.getSentenceList()

obj2 = FilterPyDocx('E:\\Documents\\PythonProjects\\1_Basics\\DataForFiles\\protest2.docx')
slist2 = obj2.getSentenceList()

finder = SimilarityFinder();
for s1 in slist1:
    for s2 in slist2:
        #print(finder.levenshtein(s1,s2))
        print("================================================================")
        print(s1)
        print("====== comparing to ==========")
        print(s2)
        print("====",finder.levenshtein(s1,s2),"====")
    







#=============================  Alternate method(Similarity of content using editdistance)  =============================

#pip install editdistance
        
import re
import zipfile
import numpy as np 
import editdistance
import pandas as pd

try:
    from xml.etree.cElementTree import XML # cElementTree is implemented in C. Much faster than python implementation
except ImportError:
    print('exception occured : Unable to use c implementation of ElementTree. Trying native implementation!!! ')
    from xml.etree.ElementTree import XML # ElementTree is implemented in Python


class FilterPyDocx:
    
    WORD_NAMESPACE = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
    PARA = WORD_NAMESPACE + 'p'
    TEXT = WORD_NAMESPACE + 't'
    paragraphs = []
    data = ''
    words = []
    filteredData = ''
    sentenceList = []
    
    
    def __init__(self,filePath):
        
        document = zipfile.ZipFile(filePath)
        xml_content = document.read('word/document.xml')
        document.close()
        tree = XML(xml_content)
        
        for paragraph in tree.getiterator(self.PARA):
            texts = [node.text for node in paragraph.getiterator(self.TEXT) if node.text]
            if texts:
                self.paragraphs.append(''.join(texts))
                sentenceEnders = re.compile('[.!?][\s]{1,2}(?=[A-Z])')
                self.sentenceList = self.sentenceList + sentenceEnders.split(''.join(texts))
                      
        self.data = '\n\n'.join(self.paragraphs)
        self.words = re.findall(r"[\w']+", self.data)
        self.filteredData = ' '.join(self.words)
        
    def getParagraphs(self):
        return self.paragraphs
        
    def getFilteredData(self):
        return self.filteredData
    
    def getWordList(self):
        return self.words
    
    def getSentenceList(self):
        return self.sentenceList
    
    
    
    
class SimilarityFinder:
    
    def findSimilarity(self,s1, s2):
        return editdistance.eval(s1,s2)
    
    
        
    
obj = FilterPyDocx('E:\\Documents\\PythonProjects\\1_Basics\\DataForFiles\\protest.docx')
slist1 = obj.getSentenceList()

obj2 = FilterPyDocx('E:\\Documents\\PythonProjects\\1_Basics\\DataForFiles\\protest2.docx')
slist2 = obj2.getSentenceList()

finder = SimilarityFinder();
similarity_table = pd.DataFrame()
ratios = [] 
result = []
for s1 in slist1:
    for s2 in slist2:
        #print(finder.levenshtein(s1,s2))
        print("================================================================")
        print(s1)
        print("====== comparing to ==========")
        print(s2)
        val = finder.findSimilarity(s1,s2)
        ratio = val/max(len(s1),len(s2))
        print("==== Ratio : ",(1-ratio),"====")
        
        
        
        
        
        
        

#==============================================================================


######################################################################################
from StringIO import StringIO
def convert(docx_data):
document = zipfile.ZipFile(StringIO(docx_data))
######################################################################################

# and handling Unicode when returning text:


content = " ".join(('\n\n'.join(paragraphs)).replace(u"\xa0", " ").strip().split())
return content


TABLE = WORD_NAMESPACE + 'tbl'
[open & read xml...]

for body in tree:
tables = body.findall(TABLE)
for table in tables:
body.remove(table)

[ rest of the code (paragraphs = []...)]




























    


