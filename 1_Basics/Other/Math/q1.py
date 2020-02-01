# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 21:21:25 2018

@author: SilverDoe
"""

import math
AB = int(input())
BC = int(input())

radangle = math.atan(AB/BC)
degangle = math.degrees(radangle)
print(str(int(round(degangle)))+'°')