'''
I am in a comment

'''

print("We are out of comment")

#Its a comment

a = 0
b = 2
print(a + b)

'''
String concatenation

'''

a = "0"
b = "23"
print(a + b)

'''
Error for incorrect data type

'''

a = "0"
b = 2
print(a + b)

'''
Casting
'''
a = 0
b = "4"
print(a + int(b))

'''
if statement
All conditional statements end with a colon
4 spaces after if
'''

a = 21

if a < 20:
    print("a is less than 20")
elif a > 20:
    print("a greater than 20")
else:
    print("a = 20")
print("End of if statement")

'''
Functions
'''

def someFunction():
    print("boo")
someFunction()

'''
function with arguement
'''

def someFunction(a,b):
    print(a+b)
someFunction(1 ,2)

'''
Global Scope function

'''

x = 10
def someFunction():
    print(x)
someFunction()

'''
For loop
'''

for a in range(1, 10):
    print(a)

'''
While loop

'''
a = 1
while a < 10:
    print(a)
    a+=1

'''
Strings
'''

myString = "ab"
print(type(myString))
print(myString)

'''
List

'''

sampleList = [1,2,3,4,5]

for a in sampleList:
    print(a)

'''
List Methods
'''
strList = [2, "abba", "cac", "dd", "ff"]

'''
Tuples
'''

myList = [1,2,3]
myList.append(4)

'''
Dictionaries
'''

myDic = {'sometime':2, 'clear': 3, 'four': 4}
print(myDic['sometime'])

print(22)

for a in myDic:
    print(a)
    print (a,myDic[a])

print('The order total comes to %f' %123.44435435)
print('The order total comes to %.3f' %123.44435435)

'''
Exceptions vs Errors

'''

var1 = '1'

try:
    var1 = var1 + 1 # since var1 is a string, it cannot be added to the number 1
except:
    print(var1 , ' is not a number \n') #so we excute this

print(var1)

'''
Reading files
'''

f = open('C:/Users/Chaitu/PycharmProjects/PythonLessons/PythonScrapFiles/init_file', 'r') # open init file
print(f.read(1))
print(f.read())
f.close()

'''
Writing files
'''
f = open('C:/Users/Chaitu/PycharmProjects/PythonLessons/PythonScrapFiles/init_file', 'r') # open init file
print(f.readline())
print(f.readline())
f.close()

'''
Using Lists to store lines
'''

f = open('C:/Users/Chaitu/PycharmProjects/PythonLessons/PythonScrapFiles/init_file', 'r') # open init file
myList = []
for lie in f:
    myList.append(lie)
print(myList)
f.close()


'''
Creating Classes
'''


from ClassOne import * #get classes from ClassOne file

myBuddy = Calculator() # make myBuddy into a Calculator object

myBuddy.add(2) #use myBuddy's new add method derived from the Calculator class

print(myBuddy.getCurrent()) #print myBuddy's current instance variable

'''
Very Large numbers
'''

# Printing 100 raise to power 100
print(100**1000)

'''
transpose
'''

M = [[1,3], [3,4], [6, 4], [7, 3]]


for row in M:
    print(row)

trans =[[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]

'''
reading files

'''

import pandas as pd
df = pd.read_table('C:/Users/Chaitu/PycharmProjects/PythonLessons/PythonScrapFiles/readtest1', sep=',')

df2 = pd.read_csv('C:/Users/Chaitu/PycharmProjects/PythonLessons/PythonScrapFiles/readtest1', header=None)

names = ['ham', 'bam', 'cam', 'lam', 'columns']
df3 = pd.read_csv('C:/Users/Chaitu/PycharmProjects/PythonLessons/PythonScrapFiles/readtest1', names=names, index_col='columns')


'''
Hierarchical indexing
'''

parsed = pd.read_csv('file:///C:/Users/Chaitu/PycharmProjects/PythonLessons/PythonScrapFiles/hmindex', index_col=['key1', 'key2'])


