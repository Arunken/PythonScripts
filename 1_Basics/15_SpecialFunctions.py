# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 09:47:35 2018

@author: SilverDoe
"""

class MyClass:
    def __init__(self, city, pin):
        print('init method invoked')
        self.city = city 
        self.pin = pin
     
obj = MyClass('Calicut',673027)

'''        
 before creating the instance of the class "__new__" method will be called. This
 method takes  parameter "class", "args", "kwargs" and  It will bind the data type
 to given class. After it will call the "__init__" method with arguments and keyword arguments.
'''

obj1 = MyClass.__new__(MyClass) # object created but not initialised 
print(type(obj1))

obj1.city ## object not initialised >> error

obj1.__init__("calicut", "673027") # object initialized

obj1.city



#Another name for a special function/magic method is a dunder
'''
Binary Operators:
-----------------

Operator                            Method
-----------------------------------------------------                   
+                       object.__add__(self, other)
-                        object.__sub__(self, other)
*                        object.__mul__(self, other)
//                       object.__floordiv__(self, other)
/                        object.__div__(self, other)
%                      object.__mod__(self, other)
**                      object.__pow__(self, other[, modulo])
<<                     object.__lshift__(self, other)
>>                     object.__rshift__(self, other)
&                       object.__and__(self, other)
^                       object.__xor__(self, other)
|                        object.__or__(self, other)

Assignment Operators:
---------------------

Operator                        Method
-----------------------------------------------------
+=                     object.__iadd__(self, other)
-=                      object.__isub__(self, other)
*=                      object.__imul__(self, other)
/=                      object.__idiv__(self, other)
//=                     object.__ifloordiv__(self, other)
%=                    object.__imod__(self, other)
**=                     object.__ipow__(self, other[, modulo])
<<=                   object.__ilshift__(self, other)
>>=                   object.__irshift__(self, other)
&=                     object.__iand__(self, other)
^=                      object.__ixor__(self, other)
|=                      object.__ior__(self, other)

Unary Operators:
-----------------

Operator                        Method
------------------------------------------------------
-                       object.__neg__(self)
+                      object.__pos__(self)
abs()                object.__abs__(self)
~                      object.__invert__(self)
complex()        object.__complex__(self)
int()                  object.__int__(self)
long()               object.__long__(self)
float()               object.__float__(self)
oct()                object.__oct__(self)
hex()               object.__hex__(self)

Comparison Operators:
----------------------

Operator                        Method
-----------------------------------------------------
<                      object.__lt__(self, other)
<=                    object.__le__(self, other)
==                    object.__eq__(self, other)
!=                     object.__ne__(self, other)
>=                    object.__ge__(self, other)
>                      object.__gt__(self, other)

'''



# ======================= Overloading operators ===============================


class Calculator(object):
    def __init__(self, *args):
        """ Create a vector, example: v = Vector(1,2) """
        if len(args) == 0:
             self.values = (0,0)
        else:
             self.values = args

    def __add__(self, other):
        """ Returns the vector addition of self and other """
        added = tuple(a + b for a, b in zip(self.values, other.values) )
        return Calculator(*added)
    
c1 = Calculator(1, 2)
c2 = Calculator(10, 13)
c3 = c1 + c2
c3.values




































