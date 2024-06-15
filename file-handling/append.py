f=open("n1.txt",'a')
print(f.mode)
f.write("--hello world-")

data=('my name is jyoti\n','i am from bhopal\n','i learn pyhton\n','start from infinity\n')
f.writelines(data)

print(f.writable()) 