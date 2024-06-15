#==============================ADVANCE PYTHON=======================================

####=======HIGHER ORDER FUNCTION---->

'''higher order function works on collection of objects'''

#map is not use when we have to make choices
'''my_list=[10,20,30,40,50]   #o/p:[15,5,35,45,55]
new_list=[]
for i in my_list:
    x=i+5
    new_list.append(x)
print(new_list)'''

# my_list=[10,20,30,40,50]   #o/p:[15,5,35,45,55]
# new_list=[]
# for i in my_list:
#     x=i*i
#     new_list.append(x)
# print(new_list)


# py_list=[5,10,15,20,25]
# def add(n):
#     if n%2==0:
#         return 'even'
#     else:
#         return 'odd'
# x=list(map(add,py_list))
# print(x)

#==================================MAP===================================
'''without loop  using map function
syntax:
          map(fun_name,collection)'''

# my_list=[10,20,30,40,50]  
# def add(n):
#     return n+5
# x=map(add,my_list)
# print(x)
# print(list(x))
# #print(tuple(x))

'''my_list=[10,20,30,40,50]  
def add(n):
    return n*n
x=map(add,my_list)
print(x)
print(list(x))'''

'''string to asscii'''

# n=input("enter name:")
 
# for i in n:
#     x=ord(i)
#     print(x)

'''add 5 then asscii to character'''

# n=input("enter name:")
 
# for i in n:
#     x=ord(i)
#     s=x+5
#     print(chr(s))


'''x=input("enter name:")

def add(n):
    x=ord(n)
    y=x+5
    return(chr(y))

y=map(add,x)
print(list(y))'''

######===============FILTER()===================
'''my_list=[10,15,20,25,30,35]

def greater(n):
    if n>=20:
        return True
x=filter(greater,my_list)
print(list(x))'''

# my_list=[10,15,20,25,30,35]

# def greater(n):
#     if n%2!=0:
#         return True
# x=filter(greater,my_list)
# print(list(x))

'''my_list=[10,15,20,25,30,35]

def greater(n):
    if n%2==0:
        return True
x=filter(greater,my_list)
print(list(x))
'''
#the function which donot have name and canot be called again known as lambda.

# my_list=[5,10,15,20,25]
# def add(n):
#     if n%2==0:
#         return True
# x=list(filter(add,my_list))
# print(x)

# my_list=[5,10,15,20,25]
# def add(n):
#     if n%2!=0:
#         return True
# x=list(filter(add,my_list))
# print(x)

my_list=[5,10,15,20,25]
count=0
i=1
def add(n):
    for i in my_list:
        if n%i==0:
            count=count+1
            if count==1:
                return True
x=list(filter(add,my_list))
print(x)
