

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
                

t = TextReader('E:\\Documents\\PythonProjects\\1_Basics\\DataForFiles\\file1.txt')
#print(t.text)  
#print(t.lines) 
#print(t.wordcount)
#t.display()
t.wordlist()

# Sorting the given elements in the alphabetic order
import collections

print("words and their counnts in the sorted order : ")
x=t.words
od = collections.orderedDict(sorted(t.getWC(x).items()))
print(od)

