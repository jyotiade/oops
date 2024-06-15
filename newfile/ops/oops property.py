#multiple and multilevel inheritence are imp for interview

'''============TYPES OF INHERITENCE=========
1.single inheritence
2.multiple inheritence
3.multilevel inheritence
'''

'''==================================SINGLE INHERITENCE===================================================='''
# class A:
#     name="viti"
#     def m1(self):
#         return "this is method"
# class B(A):
#     def m2(self):
#         print("name=",A.name)
#         print("m1=",self.m1())
# obj=B()
# obj.m2()

'''==================================MULTILEVEL INHERITENCE===================================================='''
# class A:
#     name="viti"
#     def m1(self):
#         return "this is method"
# class B(A):
#     age=45
#     def m2(self):
#         print("name=",A.name)
#         print("m1=",self.m1())
# class C(B):
#     def m3(self):
#         print("age=",B.age)
#         self.m2()

# obj=C()
# obj.m3()

'''======================MRO CONCEPT======================================='''
# MRO=method resolution order  ==depth first or left to right concept--->in which left value print


# class parent1:
#     def m1(self):
#         print("parent 1 method")
# class parent2:
#     def m1(self):
#         print("parent 1 method")
# class child(parent1,parent2):
#     def m2(self):
#         self.m1()
# obj=child()
# obj.m2()

# class parent1:
#     def m1(self):
#         print("parent 1 method")
# class parent2:
#     def m1(self):
#         print("parent 2method")
# class child(parent2,parent1):
#     def m2(self):
#         self.m1()
# obj=child()
# obj.m2()

'''=====================================MULTIPLE INHERITENCE======================================='''

# class parent1:
#     def m1(self):
#         print("parent 1 method")
# class parent2:
#     def m2(self):
#         print("parent 2method")

# class child(parent2,parent1):
#     def m3(self):
#         self.m1()
#         self.m2()
# obj=child()
# obj.m3()


# class parent1:
#     def m1(self):
#         print("parent 1 method")
# class parent2:
#     def m2(self):
#         print("parent 2method")

# class child(parent1,parent2):
#     def m3(self):
#         self.m1()
#         self.m2()
# obj=child()
# obj.m3()

'''===== method override====================='''
#super method.=super() used to call the parent class in child class when it has same method,variable,function

# class parent1:
#     def m1(self):
#         print("parent 1 method")

# class child(parent1):
#     def m1(self):
#          print("parent 2 method")
#          super().m1()        #--------------------->it is a method not function used to call the parent class having same function  in child class having same function as parent class
        
# obj=child()
# obj.m1()

'''=================================================================================================================
=======================================POLYMORPHISM========================================================
'''
# Function like print,max,len are example of POLYMORPHISM

# POLYMORPHISM= many form 
# types=overloading,overridding

'''=================================method overloading==============================================='''
# class A:
#     def new(self,a,b):
#         return a+b 
#     def new(self,a,b,c):
#         return a+b+c 

# obj=A()
# print(obj.new(23,45,45))

#obj.new(34,45)

'''#============================using default variable================='''
# class A:
#     def new(self,a=0,b=0,c=0):
#         return a+b+c 

# obj=A()
# print(obj.new(20,30,50))
# print(obj.new(20,30))
# print(obj.new(20))
# print(obj.new())

'''#===================using dispatch -->only for interview==>when have to access both function in overloading'''
'''in python we donot use overloading because in overloading a class have same name function but having different
parameters in which we only access last function or method because in overloading last method overwrite previous
all methods in stack that'''
#generally not used
from multipledispatch import dispatch
class A:
    @dispatch(int,int)
    def add(self,x,y):
        print(x+y)
    
    @dispatch(int,int,int)
    def add(self,x,y,z):
        print(x+y+z)

obj=A()
obj.add(4,6)
obj.add(3,6,7)

'''    NOTE: python doesnot support overloading
'''

#===============================OVERRIDDING=============================

class A:
    def add(self,a,b):
        print("o/p from parent class")
class B(A):
    def add(self,x,y):
        print("o/p from child ")

        super().add(3,6)
obj=B()
obj.add(3,6)