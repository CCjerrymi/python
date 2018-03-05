#func.py
import math
def getMax(first,second):
    if first > second :
    	max = first
    else:
    	max = second
    return max

list = getMax(10,11) 

#print(list)

def abs(a,b):
	return a
fun = abs(1,2)
#print(fun)

def substring(string):
	print(string)
	return string[1:len(string)]

result = substring(' abcdef ')
#print(result)

#loop for tuple
def getMin(array):
	if isinsance(array,Iterable):
	    min = array[0]
	    for value in array :
	    	if min > value :
	    		min = value
	    return min

#input the tuple
#print('enter the tuple length:')
#length = int(input())
#index = 0
#numbers = ()
#while length > 1 :
#	numbers[index] = input()
#	index += 1
#	length -= 1
#	print('%d,%d',index,length)

#List Comprehensions



