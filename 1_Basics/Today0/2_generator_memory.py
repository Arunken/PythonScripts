# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 15:55:33 2018

@author: Ourabora
"""

import memory_profiler # pip install memory_profiler
import random
import time

names = ['ram','rahim','robert','steve','modi','rahul']
des = ['doctor','actor','engineer','politician','IAS','IPS','IFS']


def name_des(people):
    result = []
    for i in range(people):
        person = {'id':i,'name':random.choice(names),'des':random.choice(des)}
        result.append(person)
    return result


def name_des_gen(people):
    for i in range(people):
        person = {'id':i,'name':random.choice(names),'des':random.choice(des)}
        yield person
        

t1 = time.clock() # generator list
people = name_des(10000) # change to list show
t2 = time.clock()

print("========================================================================")
print('Memory (after):{} MB'.format(memory_profiler.memory_usage()))
print('took {} seconds'.format(t2-t1))
'''
t3 = time.clock() # normal list
people1 = name_des(10000)
t4 = time.clock()

print('Memory (after):{} MB'.format(memory_profiler.memory_usage()))
print('took {} seconds'.format(t4-t3))
'''