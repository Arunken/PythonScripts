# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import json
import base64

data = {}
f_in = open('/home/arunken/flo.jpg', mode='rb')
imFile = f_in.read()
data['img'] = base64.encodebytes(imFile).decode("utf-8")

jsonData = json.dumps(data)
print(jsonData)

