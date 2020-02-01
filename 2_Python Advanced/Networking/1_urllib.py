

import urllib
from pprint import pprint

try:    
    response = urllib.request.urlopen('http://python.org/')
    pprint(response.read().decode('utf-8'))
    
except urllib.request.URLError as ue:
    print('unable to open url')
    
else:
    print('success')
    
    
    

    


