'''
Q1. Write a python program to compare data in two text files. 

>> compare the data in the text files line by line
>> use editdistance module to implement comparison. Install it using pip if the module is no installed already.
>> Generate a csv file as output containing 4 columns based on the comparison of each line. 
>> The columns are data1,data2,ratio,result
>> data1 column contains data from firstfile.txt line by line and viz for data2.
>> ratio should show the ratio of match between lines from first and second file.
>> result can have the following values based on the ratio:

    similar : if the ratio is greater than or equal to 50%. i.e. 0.5
    same : if the ratio is 100%. i.e. 1.
    dissimilar : if the ratio is less than 50%
    
>>  Note : Use Object oriented concepts
eg: 


firstfile.txt                                                                     secondfile.txt
--------------                                                                    ---------------

My name is Kurama                                                                 My name is Arun
I am 423 years old                                                                I am 423 years old
I like to fight                                                                   I like music
I do not exist                                                                    There is a reason why I exist


output csv
-------------

Data1                       Data2                                 ratio                        result
------                      ------                                ------                       ------

My name is Kurama            My name is Arun                      
I am 423 years old           I am 423 years old 
I like to fight              I like music
I do not exist               There is a reason why I exist



Try to do these :
-----------------

Q2. Write a python program to compare data in two excel files.


Q3. Write a python program to compare data in two word files.
'''