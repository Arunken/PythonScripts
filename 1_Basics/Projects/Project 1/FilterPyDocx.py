# -*- coding: utf-8 -*-
"""
Created on Sat May 26 09:30:34 2018

@author: SilverDoe
"""

import re
import zipfile

try:
    from xml.etree.cElementTree import XML # cElementTree is implemented in C. Much faster than python implementation
except ImportError:
    print('exception occured : Unable to use c implementation of ElementTree. Trying native implementation!!! ')
    from xml.etree.ElementTree import XML # ElementTree is implemented in Python


class FilterPyDocx:
    
    WORD_NAMESPACE = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
    PARA = WORD_NAMESPACE + 'p'
    TEXT = WORD_NAMESPACE + 't'

    def __init__(self,filePath):
        
        self.filePath = filePath
        self.paragraphs = []
        self.sentenceList = []

    def unzipDocx(self):
        self.archive = zipfile.ZipFile(self.filePath)        
        return self.archive
        
    def parseXml(self):
        xml_content = self.unzipDocx().read('word/document.xml')
        self.archive.close()
        tree = XML(xml_content)
        return tree
    
    def extractParagraphs(self):    
        for paragraph in self.parseXml().getiterator(self.PARA):
            texts = [node.text for node in paragraph.getiterator(self.TEXT) if node.text]
            if texts:
                self.paragraphs.append(''.join(texts))
                sentenceEnders = re.compile('[.!?][\s]{1,2}(?=[A-Z])')
                self.sentenceList = self.sentenceList + sentenceEnders.split(''.join(texts))
        return self.paragraphs
    
    def extractSentences(self):
        self.extractParagraphs()
        return self.sentenceList
    
    def extractWords(self):  
        data = '\n\n'.join(self.extractParagraphs())
        words = re.findall(r"[\w']+", data)
        return words