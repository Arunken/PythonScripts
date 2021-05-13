#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 09:44:05 2018

@author: arken
"""
# ============== no cuda ==================================================
from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())

import os
os.environ["CUDA_VISIBLE_DEVICES"]="1"
import tensorflow as tf
import time

n = 8000
dtype = tf.float32
with tf.device("/cpu:0"):
    matrix1 = tf.Variable(tf.ones((n, n), dtype=dtype))
    matrix2 = tf.Variable(tf.ones((n, n), dtype=dtype))
    product = tf.matmul(matrix1, matrix2)


config = tf.ConfigProto(graph_options=tf.GraphOptions(optimizer_options=tf.OptimizerOptions(opt_level=tf.OptimizerOptions.L0)))
sess = tf.Session(config=config)

sess.run(tf.global_variables_initializer())
iters = 10

sess.run(product.op)
#file_writer = tf.summary.FileWriter('/path/to/logs', sess.graph)
start = time.time()
for i in range(iters):
    sess.run(product.op)
end = time.time()
ops = n**3 + (n-1)*n**2 # n^2*(n-1) additions, n^3 multiplications
elapsed = (end - start)
rate = iters*ops/elapsed/10**9
print('\n %d x %d matmul took: %.2f sec, %.2f G ops/sec' % (n, n,
                                                            elapsed/iters,
                                                           rate,))




#========================= cuda support =======================================

import os
os.environ["CUDA_VISIBLE_DEVICES"]="1"
import tensorflow as tf
import time

from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())

n = 8000
dtype = tf.float32
with tf.device("/GPU:0"):
    matrix1 = tf.Variable(tf.ones((n, n), dtype=dtype))
    matrix2 = tf.Variable(tf.ones((n, n), dtype=dtype))
    product = tf.matmul(matrix1, matrix2)

config = tf.ConfigProto(graph_options=tf.GraphOptions(optimizer_options=tf.OptimizerOptions(opt_level=tf.OptimizerOptions.L0)))

with tf.Session(config=config) as sess1:
    sess1.run(tf.global_variables_initializer())
    iters = 10
    start = time.time()
    for i in range(iters):
        sess1.run(product)   
end = time.time()
ops = n**3 + (n-1)*n**2 # n^2*(n-1) additions, n^3 multiplications
elapsed = (end - start)
rate = iters*ops/elapsed/10**9
print('\n %d x %d matmul took: %.2f sec, %.2f G ops/sec' % (n, n,
                                                                elapsed/iters,
                                                                rate,))































