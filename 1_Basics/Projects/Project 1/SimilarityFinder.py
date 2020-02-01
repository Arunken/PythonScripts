# -*- coding: utf-8 -*-
"""
Created on Sat May 26 09:32:36 2018

@author: SilverDoe
"""
import editdistance

class SimilarityFinder:
    
    def __init__(self, sourceList, targetList):
        self.sourceList = sourceList;
        self.targetList = targetList;
        self.ratios = []
        self.results = []
        
    
    def ratres(self):
        for s1, s2 in zip(self.sourceList, self.targetList):
            diff = editdistance.eval(s1,s2)
            ratio = 1-(diff/max(len(s1),len(s2)))
            
            self.ratios.append(ratio)
            if ratio<0.5:
                self.results.append('Dissimilar')
            elif ratio<1:
                self.results.append('Similar')
            else:
                self.results.append('Duplicate')
        return self.ratios,self.results
    