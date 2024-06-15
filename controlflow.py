
#=======================================CONTROL-FLOW===========================================
'''
1.CONDITIONAL STATEMENT:
  i) if 
  ii) if-else
  iii) if-elif-else

2.TRANSFER STATEMENT: 
   i)continue
   ii)break
   iii)pass

3.ITERATIVE STATEMENT: 
   i)for
   ii)while
'''

#===================================    **************CONDITIONAL STATEMENT****************     =====================================
'''
if
if-else
if-elif-else
'''
#==================================IF STATEMENT===========================================
'''  if(Condition):
            ________(statement1)
            ________
        (break block)
        print(statement 2)

        we can use if statement without else .
'''

  #---------input function always take string datatype bydefault
'''
# x=input("enter your age")             
# print(type(x))
# print(x)
# y=int(input("enter age"))   #int,float,complex
# print(type(y))

# z=int(input("enter age:"))
# if z>=18:
#     print("you can vote")
#     print("weldone")
# print("thanks visiting")
'''

#==============================IF-ELSE STATEMENT============================
'''
==========================>FOR SINGLE CONDITION
if condition:
    statement1
else:
    statement2
    
'''
# x=int(input("enter your age"))
# if x>=20:
#     print("yes")
# else:
#     print("no")     


#===============================IF-ELIF-ELIF-ELSE===============================

'''
====================>FOR MULTIPLE CONDITION
if condition:
    statement1
elif condition2:
    statem2
elif condtion3:
    ste3
else:
'''
# y=int(input("enter your age"))   #intendation used to start block it doesnot use{}.
# if y>=60:
#     print("counter1")
# elif y>=40:
#     print("counter2")
# elif y>=20:
#     print("counter3")
# else:
#     print("nothing")


#===================================  ***********ITERATIVE STATEMENT*************** ==============================

#=====While=------------------------------>: 
     # if we donot use increment and decrement in while loop it run infinite times.

     # always asked output in horizontal way in python
'''
   initilize
   while(condition):
          true block
          statement
          increment/decrement
          '''
'''
# x=1
# while x<=10:
#     print(x)
#     x=x+1


# n=int(input("enter no"))
# i=1
# while i<=n:
#     # print(i)
#     print(i,end=",")    #end used to end the line and print output in same line
#     i=i+1


# m=int(input("enter no"))
# i=1
# while i<=m:
#     if i<=(m-1):
#         print(i,end=",")
#     else:
#         print(i)
# i=i+1

# n=int(input("enter no:"))
# i=1
# while i<=n :
#     if i%2==0:
#         print(i,end=",")
    
#     i=i+1


# m=int(input("enter no:"))
# i=1
# while i<=m :
#     if i%2!=0:
#         print(i,end=",")
    
#     i=i+1

# n=int(input("enter no:"))
# i=1
# s=0
# while i<=n:
#     if i<=n-1:
#         print(i,end="+")
        
#     else:
#         print(i,end="=")
#     s=s+i
#     i=i+1  
# print(s)


# n=int(input("enter no:"))
# i=1
# s=0
# while i<=n :
#     if i%2==0 and i<=n-1:
#         print(i,end="+")
#     else:
#         print(i,end="=")
#     s=s+i
#     i=i+1
# print(s)

'''
#=====FOR LOOP------------------------------>

#range: it is in-built function not a method
'''
   range(start,end,step)
   range(end)
   range(start,end)
   '''
# x=range(5)
# print(x)
# print(list(x))
# print(tuple(x))

# n=int(input("enter no"))
# x=range(2,n,2)
# print(list(x))
# y=range(2,n,-2)
# print(list(y))

#=====for loop-----------> donot use increment /decrement
'''
# for i in range(1,11):
#     print(i)
#     print("helllo")
'''

'''n=int(input("enter no:"))
for i in range(1,n+1):
    if i<n:
        print(i,end=",")
    else:
        print(i,end="")'''
# n=int(input("enter no:"))
# s=0
# for i in range(1,n+1):
#     s=s+i
#     if i<n:
#         print(i,end="+")
#     else:
#         print(i,end="=")
# print(s)

          
# n=int(input("enter no="))
# for i in range(1,n+1):
#     if i%2==0 :
#         if(i<=n-1):
#             print(i,end=",")
#         else:
#             print(i)


'''  
# n=int(input("enter no="))
# for i in range(1,n+1):
#     if i%2!=0 :
#         if(i<=n-1):
#             print(i,end=",")
#         else:
#             print(i)
   
'''

'''n=int(input("enter no="))
s=0
for i in range(1,n+1):
    if i%2==0 :
        if(i<=n-1):
            print(i,end="+")
        else:
            print(i,end="=")
        s=s+i
print(s)'''

# n=int(input("enter no="))
# s=0
# for i in range(1,n+1):
#     if i%2==0 :
#         s=s+i
#         if(i<=n-1):
#             print(i,end="+")
#         else:
#             print(i,end="=")
        
# print(s)
'''
n=int(input("enter no="))
s=0
for i in range(1,n+1):
    if i%2!=0 :
        if(i<=n-2):
            print(i,end="+")
        else:
            print(i,end="=")
        s=s+i
print(s)
'''

# n=int(input("enter no="))
# for i in range(1,n+1,1):
#     if(i<n):
#             print(i,end=",")
#     else:
#             print(i)


# n=int(input("enter no="))
# for i in range(1,n+1,2):
#     if(i<=n-2):
#             print(i,end=",")
#     else:
#             print(i)


# n=int(input("enter no="))
# for i in range(2,n+1,2):
#     if(i<=n-2):
#             print(i,end=",")
#     else:
#             print(i)

#=====>while loop
# n=int(input("enter natural number"))
# sum=0
# i=1
# while(i<=n):
   
#     # if i<=n-1:
#     #     print(i)
#     # else:
#     #     print(i)
#     sum=sum+i
    
#     if i<=n-1:
#         print(sum,end=",")
#     else:
#         print(sum)
#     i=i+1

#======>for loop
'''# sum=0
# for i in range(1,11):
# #print(i,end="->")
#     sum=sum+i
#     if i<=n-1:
#         print(sum,end=",")
#     else:
#         print(sum)

'''

#=====================ARMSTRONG NUMBER=========:======>
'''n=int(input("enter armstrong number"))
sum=0
m=n
count=len(str(n))
while m>0:
    r=m%10
    #k=r**count
    sum=sum + (r**count)
    m=m//10
if sum==n:
    print("number armstrong")
else:
    print(" not armstrong")
'''

#=================PRIME NUMBER=======================>

# n=int(input("enter no:"))
# i=1
# count=0
# while i<n:
#     if n%i==0 :
#         count=count+1
#     i=i+1
# if count==1:
#     print("prime number")
# else:
#     print(" not prime no")

      


n=int(input("enter no:"))
i=1
count=0
while i<n:
    if n%i==0 :
        count=count+1
        if count>1:
            break
    i=i+1
if count==1:
    print("prime number")
else:
    print(" not prime no")
      

