#==========================string=======================================#
'''
s="name"
print(type(s))
str="viti"
print(type(str))
print(str.index('t'))

st="i 'love' python"
print(st)
r='i "love" python'
print(r)

t=''' 'i' 'like' "python" '''
print(t)

str1="re"
str2="start"
print(str1+str2)
print(str1+''+str2)

x="b"
y="d"
z="t"
print(ord(x))
print(len(str2))
print(max(str2))

v="viti"
print(len(v))
for i in v:
    print(ord(i))
c=ord(i)
print(chr(c))


strin="startover"
print(strin.split('t',2))
'''


#======================================================================== LIST ====================================================#

'''
lis=[10,30,50,40,67]
lis[0]=90
print(lis)

tup=(20,30,40,70)
n=list(tup)
print(n)
print(type(n))

li=[23,4,5,66,76,8]
print(len(li))
print(max(li))
print(min(li))
print(id(li))
print(sum(li))

#==============method=============
#append
my_list=[34,45,6,77,7,44]
my_list.append(89)
print(my_list)
my_list.append([34,45,667,65])  #to add object
print(my_list)

#clear
#print(my_list)

h=[]
print(type(h))

#copy
my_list.copy()
print(my_list)
z=my_list.copy()
print(type(z))

x=[34,546,67,788,88,55]
y=x
print(y)
x.remove(67)
print(y)

y=x.copy
print(y)

print(id(x))
print(id(y))

#count() =>means how many time object come in list
print(my_list.count(44))  #frequency

#extend()
my_list1=[45,66]
my_list.extend(my_list1)  #to add list
print(my_list)
my_list1.extend(my_list)
print(my_list1)

#insert
my_list.insert(3,500)
print(my_list)

#pop()  =>to remove last element
my_list.pop()
print(my_list)

#remove() => to remove element from any position in list
my_list.remove(77)
print(my_list)

#sort()
my_list.sort()
print(my_list)
my_list.sort(reverse=True)
print(my_list)

'''





#====================================================TUPLE==========================================================================#
#LIST AND TUPLE IMP
'''
my_tuple=(23,45,34,56,55,45)

#methods =>only two method is supported by tuple because in tuple we cannot change object
print(my_tuple.count(45))
print(my_tuple.index(55))

#indexing
print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[-2])

#functions
print(len(my_tuple))
print(max(my_tuple))
print(min(my_tuple))
print(sum(my_tuple))
print(id(my_tuple))
print(type(my_tuple))

#slicing
print(my_tuple[1:3])

#conversion list into tuple and tuple onto list
x=list(my_tuple)
print(type(x))
x[0]=70
print(x)
print(tuple(x))
y=tuple(x)
print(type(y))
'''

#=====================================================  DICTONARY==================================================#

x=dict()
print(type(x))

x['name']='viti'
print(x)

x['name'],x['age']='viti',67
print(x)

print(x['name'])

x['age']=45
print(x)

x['name']='niti'
print(x)

y=dict()
y['name'],y['age'],y['place']='jyoti',22,'mumbai'
print(len(y))
print(id(y))
print(type(y))

#method

my_dict={'name':'viti','age':21,'city':'mumbai'}
# my_dict.clear()
# print(my_dict)

print(my_dict.keys())     #for any value
print(my_dict.values())

print(my_dict.keys)  #for memory location

print(my_dict.items)  #location
print(my_dict.items())

print(my_dict.pop('name')) #delete iteam
print(my_dict)
print(my_dict.popitem())

# del my_dict['city']  #no blank dict exist
# print(my_dict)

my={'name':'viti','age':21,'city':'mumbai'}
z=my
z=my.copy()
print(id(my))
print(id(z))
print(my_dict.copy())
del my['name']
print(z)