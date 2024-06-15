'''#======================OOPS================================='''

#oops used to add real world entities in our programming language.

#class is define as a bluprint of object in which we define properties,actions and behaviour of object.
#object is define as the instance of class or existence of class

#learn real world examples of all oops concept
 
#      variables: instance,local,static
#      methods:  instance,local,static

'''====================calling of class without using constructor==================='''

# class student:
#     stu_quali="b.tech"

#     def stu_detail(name,age):
#         print("studentname:",name)
#         print("studentage:",age) cvx
#         print("stu_qualification:",student.stu_quali)

# obj=student
# obj.stu_detail("viti","19")         # or  student.stu_detail("viti",20)

'''magic method==_ _init_ _ (which contain underscore)

constuctor is specical type of method which automatically called while making object we donot have to call it
_ _init_ _ is predefined constructor '''

'''==========================calling class with constructor=========================='''

# class student:
#     #stu.qual="b.tech"

#     def __init__(self):
#         print("constuctor called")
# obj=student()   # --->responsible to call constructor
# print(obj)

'''==============================vaiable====================================================='''

'''variable with self are known as instance variable
any method which first parameter is self is called instance method'''

# class student:
#     stu_quali="b.tech"

#     def stu_detail(self,name,age):
#         print("studentname:",name)
#         print("studentage:",age)
#         print("stu_qualification:",student.stu_quali)

# obj=student()
# obj.stu_detail("viti","19")         # or  student.stu_detail("viti",20)

