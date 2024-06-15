#==============tell() and seek()=======================

# f=open('n1.txt','r')
# print(f.tell())

# print(f.read(3))
# f.seek(0)

# print(f.read(10))
# print(f.tell())

# f.seek(15)
# print(f.tell())

'''o index means from starting cursor move,
1 positive means from current position cursor move,
2 negative means from last position' cursor move'''

# f=open('n1.txt','rb')     #binary
# print(f.tell())

# f.seek(-10,2)   #2 for last,negative indexing
# print(f.tell())

# print(f.read(10))  #b''==>b stand for binary and '' blank string
# print(f.read(10))

'''with open  -> is used in file handling to close file automatically ,it is inbuilt'''

with open('n1.txt','r') as f:
    print(f.read(10))
    print(f.tell())
    f.seek(10)
    print(f.tell())
    print(f.closed)

print(f.closed)