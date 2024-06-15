#=============LAMBDA FUNCTION=====================================

'''function without name
also called ananoymous function
lambda keyword used to define lambda function'''

'''syntex:
               lambda (arguments):expression
                 !       !
             keyword    multiple inputs
'''

# x=lambda name:print("hello",name)
# x("jyoti")

# x=lambda x,y:x+y
# print(x(10,34))

# x=lambda name:print("hello",name)
# y=input("entwe name:")
# x(y)

# x=lambda x,y:x+y
# p=int(input("enter no"))
# q=int(input("enter no"))
# print(x(p,q))

'''lambda with map'''
# my_list=[2,4,6,8,10]
# x=list(map(lambda x:x**2,my_list))
# print(x)

'''lambda with filter'''
# my_list=[1,2,3,4,5,6,7,8,9,10]
# x=list(filter(lambda x:x%2==0,my_list))
# print(x)

# my_list=[1,2,3,4,5,6,7,8,9,10]
# x=list(filter(lambda x:x%2!=0,my_list))
# print(x)

'''=============================REDUCE()============================================='''
#=======**from functool import reduce

from functools import reduce

# my_list=[10,30,15,25,30,50,80,60,70]
# def max(x,y):
#   if x>y:
#     return x
#   else:
#     return y
# x=reduce(max,my_list)
# print(x)


# my_list=[10,30,15,25,30,50,80,60,70]
# def max(x,y):
#   if x<y:
#     return x
#   else:
#     return y
# x=reduce(max,my_list)
# print(x)


# my_list=[10,30,15,25,30,50,80,60,70]
# def max(x,y):
#   return x+y
# x=reduce(max,my_list)
# print(x)

# my_list=[2,4,6,10,8,7,9,35,25]
# def max(x,y):
#   if x<y:
#     return x
#   else:
#     return y
# x=reduce(max,my_list)
# print(x)



# def fac(n): 
#   f=1
#   for i in range(1,n+1):
#     f=f*i
#   return f
# n=int(input("enter no"))
# print("factorial=",fac(n) )

# def fac(n): 
#   f=1
#   for i in range(1,n+1):
#     f=f*i
#   return f
# n=int(input("enter no"))
# m=int(input("enter no"))
# p=int(input("enter no"))
# lis=[n,m,p]
# x=list(map(fac,lis))
# print((x)) 