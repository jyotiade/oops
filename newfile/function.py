# function  is used for reuseability of code 
#diff b/w loop and function
#1.function has to call but we donot have to call loop
#2.in loop therir is no reuseability of code but in function it is

'''in-built function
print()    type()
max()      int()
min()      str()
sum()
len()
id()'''

'''userdefined function

syntax: 
         
         def functionname(parameters):       #parameter when variable  are used when it is made
             body
             return
        functionname(argument)   #argument when variable are used while calling function'''

# def add(x,y):
#     z=x+y
#     return z
# x=add(20,30)
# print(x)

'''p=int(input("enter 1 no"))
q=int(input("enter 2 no"))
def add(x,y):
   z=x+y
   return z
r=add(p,q)
print(r)
'''

# def add(x,y):
#    z=x+y
#    print(z)
#    #print(x+y)
# p=int(input("enter 1 no"))
# q=int(input("enter 2 no"))
# add(p,q)

'''def add(x,y):
   z=x+y
   print(z)
   #print(x+y)
p=int(input("enter 1 no"))
q=int(input("enter 2 no"))
print(add(p,q))'''

#when in single line we use print two time then it give ans with none where 1 print (internal)give 40 and second print give none

# def add(x=0,y=0):
#    z=x+y
#    print(z)
#    #print(x+y)
# p=int(input("enter 1 no"))
# # q=int(input("enter 2 no"))
# add(p)

'''def add(x,y):
   z=x+y
   print(z)
   #print(x+y)
p=int(input("enter 1 no"))
# q=int(input("enter 2 no"))
add(p)
'''

# def add(x):
#    z=x+y
#    print(z)
#    #print(x+y)
# p=int(input("enter 1 no"))
# q=int(input("enter 2 no"))
# add(p,q)

'''in ideal condition no. of parameter=no. of argument'''

# def square(x):
#    square=x**x
#    print(square)
# z=int(input("enter no"))
# print("hello")
# square(z)

'''x=50
print(print(print(x)))    o/p= 50 none none'''

'''for multiple argument as input for add function'''
# def add(*x):
#    add=0
#    for i in x:  
#       add=add+i
#    print("add=",add)
# add(10,20)
# add(10,20,30,40,50,60)

'''def employee_data(**data):
   for i,j in data.items():
      print(i,"=",j)
      #print(j)
      #print(i)
employee_data(name="jyoti",city="bhopal")'''





#==================================================================================================================
#==================================================****SCOPE****==================================================
# =>local--->within scope or body
# =>global---->outside scope

#local===>
 #=>local--->within scope or body
'''def add(x):
   y=10
   sum=x+y
   print(sum)
add(10)
print(y)'''
#---------------------------------
#global
# =>global---->outside scope
'''y=10
def add(x):
   sum=x+y
   print(sum)
add(10)
print(y)
'''
#-------------------------------------
 #===local variable has priority among gloabal and local
'''y=10     
def add(x):
   y=30
   sum=x+y
   print(sum)
add(10)
print(y)
'''
#----------------------------------
##=== globals()[''] method is used to prioritized the global variable in scope ,it is inbuilt method
'''y=10     
def add(x):
   y=30
   sum=x+globals()['y']
   print(sum)
add(10)
print(y)'''

#----------------------------------
#===to access local variable outside its scope  we use global keyword
'''def add(x):
   global y    
   y=10
   sum=x+y
   print(sum)
add(10)
print(y)'''
#-------------------------------------
 #=== in this case global y variable overwrite the global variable outside the scope and print value y=20
'''y=20
def add(x):
   global y   
   y=20
   sum=x+y
   print(sum)
add(10)
print(y)'''
#---------------------------------------
#=== in this case global y variable donot overwrite the global variable outside the scope when it write above the callback function and print value y=20
'''y=20
def add(x):
   global y    
   y=20
   sum=x+y
   print(sum)
y=30
add(10)
print(y)'''
#---------------------------------------------
#if it write below the call  back function then it overwrite the value of y and print y=30
'''y=20
def add(x):
   global y    
   y=20
   sum=x+y
   print(sum)
add(10)
y=30
print(y)'''


#========================calculator==================================


# def add_sub_mul_div(x,y):
#    add=x+y
#    print(add)
#    sub=x-y
#    print(sub)
#    mul=x*y
#    print(mul)
#    div=x/y
#    print(div)
# print("1.add\n""2.sub\n""3.mul\n""4.div\n""5.break\n")

# n=int(input("enter your choice="))  
# while True:
#    if n in (1,2,3,4):
#       p=int(input("enter 1 no"))
#       q=int(input("enter 2 no"))

#       if(n==1):
#          add_sub_mul_div(p,q)
#       elif(n==2):
#          sub(p,q)
#       elif(n==3):
#          mul(p,q)
#       elif(n==4):
#          div(p,q)
#    elif(n==5):
#       break

 #==========================================CALCULATOR=============================================================  
def add(x,y):
   add=x+y
   print(add)

def sub(x,y):
   sub=x-y
   print(sub)

def mul(x,y):
   mul=x*y
   print(mul)

def div(x,y):
   div=x/y
   print(div)

while True:
   print("1.add\n""2.sub\n""3.mul\n""4.div\n""5.break\n")

   n=int(input("enter your choice="))
   if n in (1,2,3,4):
      p=int(input("enter 1 no"))
      q=int(input("enter 2 no"))
      if (n==1):
         add(p,q)
      elif(n==2):
         sub(p,q)
      elif(n==3):
         mul(p,q)
      elif(n==4):
         div(p,q)
   elif(n==5):
      break
   else:
      print("invalid")


