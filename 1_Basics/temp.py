# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

values = [[3,4,5,1],[33,6,1,2]]

for row in values:
    row.sort()
    for element in row:
        print(element,end=" ")
        
values = [2,3,2,4]
def my_transformation(num):
    return num**2
for i in map(my_transformation,values):
    print(i)      
    
m = [[x,y] for x in range(0,4) for y in range(0,6)]

list1 = list([1,2,3])

list2=[]
list3 = list()


def example(a):
    a = a+'2'
    a = a*2
    return a

example("hello")

ng = {}
ng[(1,2,4)]=8
ng[(4,2,1)]=10
ng[(1,2)]=12

sum=0
for k in ng:
    sum = sum+ng[k]
    
print(len(ng)+sum)


x =['ab','cd']
print(list(map(upper,x)))

def foo(x):
    x = ['def','abc']
    return id(x)
q = ['abc','def']
print(id(q)==foo(q))


n=round(6352.898,2)



for i in [1,2,3,4][::-1]:
    print(i)
    
for i in range(0):
    print(i)
    
b=['niit']*4

names = ['sas','ttr']

print("\n".join(names))



d1 = {"john":40,"peter":45}
d2 = {"john":446,"peter":45}

d1>d2

values=[1,2,1,3]
nums=set(values)
def checkit(num):
    if num in nums:
        return True
    else:
        return False
for i in filter(checkit,values):
    print(i)



try:
    list = 10*[0]
    x = list[9]
except IndexError:
    print("Index out")
else:
    print("Wrong")
finally:
    print("finally")

def foo():
    try:
        print(1)
    finally:
        print(2)



foo()


class A:
    def__init__(self):
        self.x=1
        self.__y=1
        
    def getY(self):
        return self.__y
    
a = A()
print(a.x)

def foo():
    return total+1
total=0
print(foo())















print('1.1'.isnumeric())



















