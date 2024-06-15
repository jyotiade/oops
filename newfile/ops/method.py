'''========================================METHOD================================================================'''

'''####===================instance method====>to access one instance method into another instance method==========================='''

# class student:

#     def display(self,name):
#         self.name=name
#         print("name=",self.name)
    
#     def show(self,age):
#         self.age=age

#         self.display("niti")
#         print("age=",age)

# obj=student()
# obj.display("viti")
# obj.show(21)

 #student.display("jyoti")    ===>it give positional error and canot access with class name beacause we make the object of class

'''==================================class method======>to modify the static variable=============================================='''
#cls -->represent class

'''class method:
    1. @classmethod
    2.instead of self,here we use cls'''

# class book:

#     price=1000

#     def book_detail(self,name,author):
#         self.name=name
#         self.author=author
    
#     @classmethod       #===================>universal cls use for class method  ==>@ is decoretor==>it change value
#     def update_detail(cls,price):
#         cls.price=price
    
#     def show_detail(self,page):
#         self.page=page
        
#         print("book name=",self.name)
#         print("book author=",self.author)
#         print("book price=",book.price)
#         print("book pages=",self.page)

# obj=book()
# obj.book_detail("pyhton","G.R")
# obj.update_detail(2000)
# #obj.show_detail()
# obj.show_detail(120)


'''=====================================================static method=============================================='''

class student:
    @staticmethod
    def great():
        print("thank for visit")
    
    def great1(self):
        print("welcome")
        
obj=student()
obj.great()
student.great()
#student.great1()
obj.great1()

'''# if we donot make object constructor then we donot call it with the help of object to call it with object 
# we have to make the great1 function intance function and has to pass self in that function to call it 
# with the help of object
'''