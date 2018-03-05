#stage1.py


#list
list1 = range(10)
for index,value in enumerate(list1):
	print('list1 index=%d value=%s'%(index,value));

list2 = [["cpu","memory"],["harddisk","soundcard"]];
for i in range(len(list2)):
    list3 = list2[i];
    for j in range(len(list3)):
    	print(list3[j]);


#tuple
t = ('c++','java','c#','python');
for index,value in enumerate(t):
    print(index,value);

#key & value
d = {'age':'18','name':'jack','sex':'male'};
print('get all values')
for value in d.values():
	print(value);

print('get all keys')
for key in d.keys():
	print(key);

print('get the value of key age')
print(d['age']);