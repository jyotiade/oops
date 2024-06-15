#f is a universable variable to open file
#it is convinient to write functioin in data variable and then print variable

f=open('n1.txt','r')  #or open('n1.txt')-->by default it is in read mode
print(f.mode)
# data=f.read()
'''output:r'''

# print(data)
'''output:
-----hello--------my name is jyoti
i am from bhopal
i learn pyhton
start from infinity'''

# f.close()
# print(f.read())
# print(f.read(10))
'''output:-----hello'''

# print(f.read(50))
'''output:
-----hello
--------my name is jyoti
i am from bhopal
i learn'''

# print(f.readline())  #single line data
'''output:-----hello--------my name is jyoti'''

# print(f.readlines())  #multiple line data
'''output:['-----hello--------my name is jyoti\n', 'i am from bhopal\n', 'i learn pyhton\n', 'start from infinity\n']'''

print(f.readable())
'''output:True'''
