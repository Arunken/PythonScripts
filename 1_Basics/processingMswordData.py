# -*- coding: utf-8 -*-
"""
Created on Thu May 24 13:53:11 2018

@author: SilverDoe
"""


"""
Module that extract text from MS XML Word document (.docx) and store as list
"""

import re
import zipfile

try:
    from xml.etree.cElementTree import XML # cElementTree is implemented in C
except ImportError:
    from xml.etree.ElementTree import XML # ElementTree is implemented in Python

''' 
>>> If you can, use the C implementation because it is optimized for 
    fast parsing and low memory use, and is 15-20 times faster than the Python implementation.
    
>>> Use the Python version if you are in a limited environment (C library loading not allowed)

'''




WORD_NAMESPACE = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
PARA = WORD_NAMESPACE + 'p'
TEXT = WORD_NAMESPACE + 't'


def get_docx_text(path):
    """
    Take the path of a docx file as argument, return the text in unicode.
    """
    document = zipfile.ZipFile(path)
    xml_content = document.read('word/document.xml')
    print(type(xml_content))
    document.close()
    tree = XML(xml_content)
    print(tree)

    paragraphs = []
    for paragraph in tree.getiterator(PARA):
        texts = [node.text for node in paragraph.getiterator(TEXT) if node.text]
        if texts:
            paragraphs.append(''.join(texts))
    
    return '\n\n'.join(paragraphs)

data = get_docx_text('E:\\Documents\\PythonProjects\\1_Basics\\DataForFiles\\protest.docx')
print(data) # Complete paragraph
words = re.findall(r"[\w']+", data) # filter out individual words and store in a list
sampledata1 = ' '.join(words)
print(sampledata1)

import pandas as pd

df = pd.DataFrame(words,columns = ['Data_A'])



#==============================================================================

import xml.etree.ElementTree as ET
import zipfile


archive = zipfile.ZipFile("E:\\Documents\\PythonProjects\\1_Basics\\DataForFiles\\protest.docx")
xml_content = archive.read('word/document.xml')
archive.close()
tree = XML(xml_content)

for paragraph in tree.getiterator(PARA):
    texts = [node.text for node in paragraph.getiterator(TEXT) if node.text]
    for node in paragraph.getiterator(TEXT):
        if node.text:
            print(node.text)
    


