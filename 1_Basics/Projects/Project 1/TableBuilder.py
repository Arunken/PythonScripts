# -*- coding: utf-8 -*-
"""
Created on Sat May 26 09:33:30 2018

@author: SilverDoe
"""

import pandas as pd

class TableBuilder:

    def __init__(self,data):
        self.df = pd.DataFrame(data)
        
    def generateCSV(self,savePath):
            self.df.to_csv(savePath,encoding='utf-8')
