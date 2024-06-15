#====create=======

# f=open("n3.txt",'x')
# print(f.mode)

#======write========
'''f=open("n3.txt",'w')
print(f.mode)
f.write("do something to make your future bright\n")

# f=open("n1.txt",'a')
# f.write("small world")

data=("beautiful things\n","comes in small packects")
f.writelines(data)
'''
#=====read============
f=open("n3.txt",'r')
# print(f.read())
print(f.read(10))
print(f.readable())