# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 23:03:37 2018

@author: SilverDoe
"""


try:
    a = 12
    b=0
    c=a/b
    print("result : ",c)
except:
    print("Some exception occured")
    
#==============================================================================
try:
    file = open('test.txt', 'rb')
except IOError as e:
    print('An IOError occurred. {}'.format(e.args[-1]))
    
    
#==============================================================================
try:
    file = open('test.txt', 'rb')
except (IOError, EOFError) as e:
    print("An error occurred. {}".format(e.args[-1]))
    
#==============================================================================
try:
    file = open('test.txt', 'rb')
except EOFError as e:
    print("An EOF error occurred.")
    #raise e
except IOError as e:
    print("An IOError occurred.")
    #raise e
    
#============================================================================== 
try:
    file = open('test.txt', 'rb')
except Exception:
    print('exception occured')
    # Some logging if you want
    #raise
    
#==============================================================================
try:
    f_in = open('E:\\mydata.txt','r',encoding='ascii')
except IOError as e:
    print('An IOError occurred. {}'.format(e.args[-1]))
finally:
    print("This would be printed whether or not an exception has occurred!")
    f_in.close()
    
#==============================================================================
try:
    print('I am sure no exception is going to occur!')
except Exception:
    print('exception')
else:
    # any code that should only run if no exception occurs in the try,
    # but for which exceptions should NOT be caught
    print('This would only run if no exception occurs. And an error here '
          'would NOT be caught.')
finally:
    print('This would be printed in every case.')
    
