# n=int(input("enter no."))

# if n>=80:
#     print("a grade")
# elif n>=60:
#     print("b grade")
# elif n>=40:
#     print("c grade")
# else:
#     print("failed")

# x=int(input("enter 1 no"))
# y=int(input("enter 2 no"))

# temp=x
# x=y
# y=temp

# print("value of x",x)
# print("value of y",y)

'''x=int(input("enter 1 no"))
y=int(input("enter 2 no"))

x,y=y,x
print("value of x",x)
print("value of y",y)
'''

# x=int(input("enterno"))
# i=1
# sum=0
# while i<=x:
#     sum=sum+i
#     if i<x:
#         print(i,end="+")
#     else:
#         print(i,end="=")
#     i=i+1
# print(sum)

#n=int(input("enter no="))

# for i in range(1,n+1):
#     if i%2==0:
#         if i<n:
#             print(i,end=",")
#         else:
#             print(i,end="")
#             n=int(input("enter no="))

'''s=0
for i in range(1,n+1):
    if i%2==0:
        s=s+i
        if i<n:
            print(i,end="+")
        else:
            print(i,end="=")
print(s)
'''
# n=int(input("enter no="))
# s=0
# for i in range(1,n+1):
#     if i%2!=0:
#         s=s+i
#         if i<n-1:
#             print(i,end="+")
#         else:
#             print(i,end="=")
# print(s)        

# n=int(input("enter no="))
# i=1
# while i<=n:
#     if i<n:
#         print(i,end=",")
#     else:
#         print(i,end="")
#     i=i+1

# n=int(input("enter no="))
# i=1
# s=0
# while i<=n:
#     s=s+i
#     if i<n:
#         print(i,end="+")
#     else:
#         print(i,end="=")
#     i=i+1
# print(s)

# n=int(input("enter no="))
# i=1
# s=0
# while i<=n:
#     if i%2!=0:
#         s=s+i
#         if i<n-1:
#             print(i,end="+")
#         else:
#             print(i,end="=")
#     i=i+1
# print(s)

# n=int(input("enter no="))
# i=1
# s=0
# while i<=n:
#     s=s+i
    
#     if i<n:
#         print(s,end=",")
#     else:
#         print(s,end="")
#     i=i+1

# n=int(input("enter no="))
# i=0
# sum=0
# m=n
# count=len(str(n))

# while m>0:
#     r=m%10
#     k=r**count
#     sum=sum+k
#     m=m//10
# if sum==n:
#     print("armstrong")
# else:
#     print("not")

# n=int(input("enter no"))
# i=1
# count=0

# while i<n:
#     if n%i==0:
#         count=count+1
        #   if count>1:
        #     break
#     i=i+1
# if count==1:
#     print("prime")
# else:
#     print("not prime")


# n=int(input("enter no"))
# a,b,c,i=0,1,0,1
# print(a,end=",")
# print(b,end=",")

# while i<=n:

#     c=a+b
#     a=b
#     b=c
#     i=i+1
#     if i<=n:
#         print(c,end=",")
#     else:
#         print(c,end="")


# year=int(input("enter"))

# if year%4==0 and year%100!=0:
#     print("leap year=",year)
# elif year%400 and year%100:
#     print("year leap year=",year)
# else:
#     print("not a leap yeaer")

# n=int(input("enetr="))
# m=n
# rev=0

# while m>0:
#     r=m%10
#     rev=(rev*10)+r
#     m=m//10

# if n==rev:
#     print("pallin")
# else:
#     print("not pallin")

#=====================================function================================

# def fact(num):
#     re=1
#     while num>=1:
#         re=re*num
#         num=num-1
#     return re
# n=int(input("enter no"))
# print("factorial of",n,"=",fact(n))
# output:
# factorial of 5 = 120   
# factorial of 4 = 24

# def add_sub(x,y):
#     add=x+y
#     sub=x-y
#     return add,sub
# p=int(input("enter no 1:"))
# q=int(input("enter no 1:"))
# x,y=add_sub(p,q)
# print("additiuon",x)
# print("sub",y)