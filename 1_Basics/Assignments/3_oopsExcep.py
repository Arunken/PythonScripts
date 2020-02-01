# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 14:27:23 2018

@author: Ourabora
"""

# 1)=============Create a class ‘Shapes’ and use method overloading to find the area of circle, rectangle/square and Cube. 
class Shapes:
    
    area =0
    
    # area of circle
    def findArea(self,r):
        self.area = 3.14*r**2
        return self.area
    
    # area of rectangle
    def findArea(self,l,b):
        self.area = l*b
        return self.area
    
    # area of square
    def findArea(self,c,x,y):
        self.area = c**2
        return self.area
    
        # area of cube
    def findArea(self,c,x,y,z):
        self.area = 6*c**2
        return self.area
    
obj = Shapes()
print('1. Circle \n2. Rectangle\n3. Square\n4. Cube\n\n')
ch = input('Enter your choice : ')

if(ch=='1'):
    rad = int(input('Enter the radius of the circle : '))
    print('Area of Circle :',obj.findArea(rad))

elif(ch=='2'):
    length = int(input('Enter the length fo the rectangle : '))
    breadth = int(input('Enter the breadth fo the rectangle : '))
    print('Area of Rectangle :',obj.findArea(length,breadth))
    
elif(ch=='3'):
    side = int(input('Enter the side of the square : '))
    print('Area of the Square : ',obj.findArea(side,1,1))
    
elif(ch=='4'): 
    side = int(input('Enter the side of the cube : '))
    print('Area of the Cube : ',obj.findArea(side,1,1,1))    
    
else:
    print('Invalid Input!!!')
  
    
# 2)=============Overload “+”, “-”operator to add/subtract coordinates of two points.

class OperatorOverload:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
        
    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        return OperatorOverload(x,y)
    
    def __sub__(self,other):
        x = self.x - other.x
        y = self.y - other.y
        return OperatorOverload(x,y)
    
obj1 = OperatorOverload(4,9)
obj2 = OperatorOverload(-2,5)
print(obj1+obj2)
print(obj1-obj2)

# 3)============Develop a class called TextReader which works as follows:


  class TextReader:
    
    lines = 0
    wordcount=0
    words=[]
    worddict ={}
    
    
    
    def __init__(self,filestr):
        
        self.file=open(filestr)
        self.text =self.file.read()
        for i in open(filestr):
            self.lines =self.lines+1
            
        self.words = self.text.split()
        self.wordcount = len(self.words)
        
    def display(self):
        print(self.text)
        
    def wordlist(self):
        print(self.words)
        
    def getWC(self,findwords):
        for word in findwords:
            self.count=0
            for w in self.words:
                if w==word:
                    self.count+=1
            #print('Occurence of ',word,' in the file is ',self.count)
            self.worddict[word] = self.count
        return self.worddict
                

t = TextReader('D:\\Documents\\PythonProjects\\1_Basics\\DataForFiles\\file1.txt')
#print(t.text)  
#print(t.lines) 
#print(t.wordcount)
#t.display()
t.wordlist()

# 4) ===========In the class created in previous question, add a function getWC() to get the count of some words which can be provided through a list sent as parameter
list1 = ['rw','all']
t.getWC(list1)

   
# 5) =========== Ask the user to enter a number until they guess a stored number correctly

class Error(Exception):
    pass

class ValueTooSmallError(Error):
        pass

class ValueTooLargeError(Error):
        pass

number =10

while True:
    try:
        num = int(input("Enter a number : "))
        if num<number:
            raise ValueTooSmallError
        elif num>number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("The value is too small, try again!")
    
    except ValueTooLargeError:
        print("This value is too large, try again!")
        
print("Congratulations ! you have guessed it correctly")


# 6) ========== Take a input from user and display reciprocal of it.  

class Error(Exception):
    pass

class NumberFormatError(Error):
        pass

class DivideByZeroError(Error):
        pass
    

try:
    snumb = input("Enter a number : ")
    if not snumb.isdigit():
        raise NumberFormatError
    elif int(snumb)==0:
        raise DivideByZeroError

    numb = int(snumb)
    rec = 1/numb
    print("Reciprocal is : ",rec)
    
except NumberFormatError:
    print("Please enter a number")
except DivideByZeroError:
    print("Division by zero is infinite, Please enter a non-zero value!")
except Exception:
    print("Exception occured : Input cannot be processed")
    
    
    
    
    
