# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 16:10:51 2018

@author: Ourabora
"""

import logging
from urllib.request import urlopen


def main():
    try:
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        logging.basicConfig(filename='E:\\Documents\\PythonProjects\\1_Basics\Today\\logfile.log',level=logging.DEBUG)
        logging.critical('we are in the main try loop')
        # mathfail 1/0
        
        if 1<2:
            logging.debug('entered into the first if statement')
            print('hello')
            
            try:
                print('inside try')
                urlopen('http://google.com').read()
            except Exception as e:
                print(e)
                logging.error('Exception occured : %s' %str(e))
                
        else:
            logging.debug('entered into the first else statement')
            print('ok')
            
    except Exception as e:
        logging.critical(str(e))
        
        
main()



import logging
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
logging.basicConfig(filename='D:\\Documents\\PythonProjects\\1_Basics\\Today\\sample.log',level=logging.DEBUG)
#logging.basicConfig(filename='example.log',level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.critical("this is a message")
logging.error('you did not')
























