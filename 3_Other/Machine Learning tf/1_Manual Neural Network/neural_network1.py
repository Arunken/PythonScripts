#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 23:35:33 2018

@author: arken
"""
import numpy as np

class Operation:
    
    def __init__(self,input_nodes=[]):
        
        self.input_nodes = input_nodes
        self.output_nodes = []
        
        for node in input_nodes:
            node.output_nodes.append(self)
            
        _default_graph.operations.append(self)# added after writing graph class
            
    def compute(self):
        pass

class add(Operation):
    
    def __init__(self,x,y):
        super.init([x,y])
        
    def compute(self,x_var,y_var):
        self.inputs = [x_var,y_var]
        return x_var+y_var
    
class multiply(Operation):
        
    def __init__(self,x,y):
        super().__init__([x,y])
        
    def compute(self,x_var,y_var):
        self.inputs = [x_var,y_var]
        return x_var*y_var
        
class matmul(Operation):
        
    def __init__(self,x,y):
        super().__init__([x,y])
        
    def compute(self,x_var,y_var):
        self.inputs = [x_var,y_var]
        return x_var.dot(y_var)
        
        
class Placeholder:
        
    def __inti__(self):
        
        self.output_nodes = []
            
        _default_graph.placeholders.append(self)
        
    
class Variable:
        
    def __init__(self,initial_value=None):
            
        self.value = initial_value
        self.output_nodes = []
            
        _default_graph.placeholders.append(self)
            
class Graph:
        
    def __init__(self):
            
        self.operations = []
        self.placeholders = []
        self.variables = []
            
    def set_as_default(self):
            
        global _default_graph
        _default_graph = self
        
#outside class
def traverse_postorder(operation):
    '''
    post order traversal of nodes. Basically makes sure computations
    are done in the correct order (Ax first, then AX + b).
    '''
    nodes_postorder = []
    def recurse(node):
        if isinstance(node,Operation):
            for input_node in node.input_nodes:
                recurse(input_node)
            nodes_postorder.append(node)
    
    recurse(operation)
    return nodes_postorder


class Session():
    
    def run(self,operation,feed_dict={}):
        nodes_postorder = traverse_postorder(operation)
        
        for node in nodes_postorder:
            
            if type(node) == Placeholder:
                node.output = feed_dict[node]
                
            elif type(node) == Variable:
                node.output = node.value
                
            else:
                #operation
                node.inputs = [input_node.output for input_node in node.input_node]
                node.output = node.compute(*node.inputs)
                
            if type(node.output) == list:
                node.outputs = np.array(node.output)
        return operation.output
   

         
g = Graph()
g.set_as_default()

A = Variable(10)
b = Variable(1)

x = Placeholder()

y = multiply(A,x)
z = add(y,b)  
                
sess = Session()
result = sess.run(operation=z,feed_dict={x:10})
                
       

# matrix mul

g = Graph()
g.set_as_default()

A = Variable([[10,20],[30,40]])
b = Variable([1,2,])

x = Placeholder()

y = matmul(A,x)
z = add(y,b)  
                
sess = Session()
result = sess.run(operation=z,feed_dict={x:10})         
                
                
                






        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        