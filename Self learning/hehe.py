max(1, 2, 3)

abs(-23.23)

pow(2, 5) #this is equvalent
2**5 #this is equvalent
2^5

#string
storm_greeting = "you're here"

#string combination
#first way
'hehe' + 'haha' +'!'
first = 'hehe' 
second = 'haha'
third = '!'

#second way
result = first + second + third


#string multiple
('ha'+'xi') * 5
 
#I/O of python
print 'What is the number', 3434

#result: What is the number 3434


#Python 2
raw_input("give me a number")

#Python 3
input("give me a number")

#result: returns a string

print('''HOW
ARE
YOU?
''')

#result: 
#HOW 
#ARE 
#YOU?

print('3\t4\t5')

#result: 3   4    5


#helper function, gives detailed the info
help(abs)


#Not ans
1 == 2 #False
not (1==2) #true

#without (), the order of the operater is
not, and, or


#converting str, int and float
#convert int to string

str(3)
#result: '3'

'3' * 4
#result: '3333'

int('3')
#result: 3

#covert into a float number
fl('456')
#result: 456.0

#cast the input string
int(raw_input("give me a number"))


#comparision operator

"abc" > "abaaa" #because 'a' is smaller than 'c'

'a' > 'A' #True

#substring checking
'abc' in 'abcba'
#result -> True


len('abd')
#result -> 3

len('hehe' + 'jiji' *3)



#substring slice
0     1  2  3  4  5  6  7  8  9 10 
l     e  a  r  n     t  o     g  o
-11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1	  	

#single index
s = 'learn to go'
s[0] 
#Ans: 'l'
s[-1] = 'o'
#Ans: 'o'
s[-2] = 'g'
#Ans: 'g'

#for the substring slicing the exclude the last digit
s[0:5]
#Ans: 'learn' #exclude the last digit ' '
s[6:7] 
#Ans: 'to'
s[9:len(s)] 
#Ans:'go'
s[:] 
#Ans: 'learn to go'

s[6] = 'd'
#error happens
#string is immutable. They cannot change

#String methods
newString = 'I am late, I am late'

newString.find('late')
#ans 5

newString.find('late', 7)
#starting from pos 7
#ans 14

newString.find('Late', 7)
#if not find
#ans -1

newString.rfind('late')
#starting from pos 7
#ans 14

s = '   I love coding   '
s.lstrip()
#ans: 'I love coding   '

s.rstrip()
#ans: '	  I love coding'

s.strip()
#ans: 'I love coding'

#String iteration
for char in s:
	print(char)

#find the same letter in the string
nString = ""
s = 'I love coding'

for char in s:
	if char in 'abcd':
		nString = nString + char 


#while loop
s = 'I love coding'
nString = ""
index = 0
while index < len(s):
	if s[index] in 'abcd':
		nString = nString + s[index]
	index += 1



#list slice rule
grades = [10, 20, 40]

grades[0]
#ans: 10

grades[0:2]
#ans: [10, 20]
#--> the exclude the last element in the list

#built in functions
max(grades)
min(grades)
sum(grades)


#methods for the list
list.append(object)
list.extend(list)
list.pop()
#remove and return the item at the end of the list

list.remove(object)
#remove the first occurrence of the object, error it not there

list.reverse()
list.sort()
#sort the list from smallest to larges

list.insert(int, object)
#insert oject at the given index, moving items to make soon


#the methods do not change the list
list.count(object)
list.index(object)
#return the index of the first occurrence of object


#example
colours = ['blue', 'yellow']
if colours.count('blue') > 0:
	colours.remove('blue')
#this way prevent the errors happens


if 'blank' in colours:
	where = colours.index('hot pink')
	colours.pop(where)
#delete the 'hot pink' in the list 



#list is mutable, so the data can be changed
list1[1] = 'hehe'
#mutable: list
#immutable: int, float, str, bool



#range in the list
#range(start, stop, step)

#example: get the odd index
s = "I love coding"
for i in range(1, len(s), 2):
	print i

#example, check the continuous elements in the list
s = "abccdeffggh"
repeats = 0
#the ending point is len(s) -1, which satisfied the s[i] == s[i+1]
for i in range(len(s)-1):
	if s[i] == s[i+1]:
		repeats = repeats + 1


#example for left rotating the element by 1 
s = "abccdeffggh"
first_item = s[0]
for i in range(1, len(s)):
	s[i-1] = s[i]

s[-1] = first_item 


#example of the nested for loop
average = []
grades = [[70, 80],[90, 100]]
for grades_list in grades:
	total = 0
	for mark in grades_list:
		total = total + mark

	average.append(total/len(grades_list))


#read line by line from the file
#python 2 needs to import the functions	
from __future__ import print_function


#python 3 do not need to import the function
directory = "/Users/lichuanr/Desktop/Python-practise/Chuanrui Li/CH13/sample.txt"
file2 = open(directory, 'r')
line = file2.readline()

print (line, end = '')
while line != '':
    line = file.readline()
    print (line, end = '')

#read all the file at one time
directory = "/Users/lichuanr/Desktop/Python-practise/Chuanrui Li/CH13/sample.txt"
file1 = open(directory, 'r')
print (file1.read())



#read all the lines in the list
lines = file1.readlines()
for line in lines:
	print(line, end='')



#write content into the file
directory = "/Users/lichuanr/Desktop/Python-practise/Chuanrui Li/CH13/sample.txt"
file1 = open(directory, 'r')
content = file1.read()



new_dir = "/Users/lichuanr/Desktop/Python-practise/Chuanrui Li/CH13/sample1.txt"
to_file = open(new_dir, 'w')
to_file.write('Copy\n')
to_file.write(content)
to_file.close()

    

#tuple -> immutable list
tup = ('a', 1, -0.2)

tup[0] ='b'
#error, since tuple is immutable

tup[0]
#ans: 'a'
tup[:2]
#ans: ('a', 1)

#one element tuples
(1,)



#Dictionary --> mutable

#definition -> key, value pair
average_grade = {'A1': 80, 'A2': 90, 'A3': 70}

#check the value for the key
average_grade['A1']
#ans: 80

#check the key exist or not
'A4' in average_grade
#ans: False
#adding key value pair
average_grade['A4'] = 85
len(average_grade)
#ans: 4

#iterate each key in the dictionary
for assignment in average_grade:
	print assignment, average_grade[assignment]

#ans:
# A1 80
# A2 90
# A3 70

#The key of dictionary is immutable
d = {'apple': 2, 5: 8}
d[[1, 2]] = 'banana' #error

d[(1, 2)] = 'banana' #right
d = {'apple': 2, 5: 8, (1, 2):'banana'}



#example of using dictionary
fruit_to_color= {
	'banana': 'yellow',
	'cherry': 'red',
	'orange': 'orange',
	'peach':'orange'}

color_to_fruit = {}
for fruit in fruit_to_color:
	color = fruit_to_color[fruit]

	if not (color in color_to_fruit):
		color_to_fruit[color] = [fruit]
	#otherwise, append fruit to the existing list
	else:
		color_to_fruit[color].append(fruit)

#ans
color_to_fruit = {
	'yellow': 'banana',
	'red': 'cherry',
	'orange': ['orange', 'peach']}




