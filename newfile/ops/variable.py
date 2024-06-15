'''======================VARIABLE========================================='''
# aisa variable jo object ka uper depend nahi hota static variable
# sia variable jo apne scope me hi use ya define ho sakta hai local variable
# aisa variable jo object ka uper depend hota hai aur jisi value object ka saath change hoti rehti hai

'''self is imp for interview'''  #==========>
'''self is reference variable of current object of current class'''

#======================using all variable======================================

# class student:
#     quali="M.tech"   #-----------------static variable

#     def __init__(self,name):
#         self.name=name
#     def display(self):
#         age=78          #-------------------local variable
#         print("name",self.name)
#         print("age",age)
#         print("quai.",student.quali)
# obj=student("viti")     #-----------------instance variable
# obj.display()

'''================================************==instance variable===*******************=========================================================='''

'''==============#HOW TO DECLARE INSTANCE VARIABLE:=>==================='''

# 1.through constructor  ==> to declare instance method inside constructor
# 2.through instance method  ===>method in which function having self
# 3.through object
# *method: in which function donot have self

'''class student:
    def display(self,name):
        self.name=name

    def show(self):
        print("name=",self.name)

obj=student()
obj.display("viti")
obj.show()'''

# class student:

#     def __init__(self,name):
#         self.name=name       #--------through constructor
    
#     def display(self,age):
#         self.age=age          #---------through instance method

#     def show(self):
#         print("nmae=",self.name)
#         print("age=",self.age)
#         print("quali=",self.quali)

# obj=student("viti")
# obj.display(34)
# obj.quali=("m.tech")         #-----------through object
# obj.show()


#======================HOW TO ACCSESS INSTANCE METHOD==========================

# 1.inside class   ====>access or call with self
# 2.outside class  ====>acess with object



'''#==========================********static variable**************======================================='''

class Student:
    quali = "M.Tech"   # static variable declare inside the class   

    def __init__(self,name,age):
        self.name = name
        self.age = age
        Student.school = "SHSS"  # static variable declare inside the constructor

    def display(self):
        Student.gread = "P.hd"   # static variable declare inside the instence variable

        print("Name = ",self.name)
        print("Age = ",self.age)
        print("Quali =",Student.quali)  # static variable access inside the class through class name
        print("School = ",Student.school) # static variable access inside the class through class name
        print("Gread = ",Student.gread) # static variable access inside the class through class name
        print("Achivment = ",Student.achivment)   # static variable access inside the class through class name

obj = Student("Neeraj",37)
Student.achivment="Gate-qualified"   # static variable declare outside of the class

print("Access through class_Name = ",Student.quali) # static variable access outside the class through class name

print("Access through object = ",obj.quali) # static variable access outside the class through object
obj.display()
print("Access through class_Name = ",Student.gread) # static variable access outside the class through class name

print("Access through class_Name = ",Student.school)# static variable access outside the class through class name

print("Access through class_Name = ",Student.achivment)# static variable access outside the class through class name
# obj.display()


'''========================================local variable========================================================='''
#declare and access

class student:
    
    def display(self):
        global a
        a=20    #local variable
        print("value=",a)     #access

    def show(self):
        print("value=",a)    #donot access

    def new():
        print("value=",a)

obj=student()
obj.display()
obj.show()

#when we donot use self then we donot call function with object then in that condition we use class name to 
#access  function
student.new()   
print("value=",a)    #donot access

