# *
# **
# ***
# ****
# *****
'''n=int(input("enter row:"))  
for i in range(1,n+1):
    print("*"*i)
'''
# *
# * *
# * * *
# * * * *
# * * * * *
'''n=int(input("enter row:"))  
for i in range(1,n+1):
    print("* "*i)
'''
#     *
#    **
#   ***
#  ****
# *****
'''n=int(input("enter row:"))  
for i in range(1,n+1):
    print(" "*(n-i)+"*"*i)'''
#     *
#    ***
#   *****
#  *******
# *********
'''n=int(input("enter row:"))  
for i in range(1,n+1):
    print(" "*(n-i)+"*"*(2*i-1))'''

#     *
#    * *
#   * * *
#  * * * *
# * * * * *
'''n=int(input("enter row:"))  
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)'''

# 1
# 12
# 123
# 1234
# 12345
'''n=int(input("enter row:"))  
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()'''
# *****
#  ****
#   ***
#    **
#     *
'''n=int(input("enter row:"))  
for i in range(n,0,-1):
    print(" "*(n-i)+"*"*i)'''

# *****
# ****
# ***
# **
# *
'''n=int(input("enter row:"))  
for i in range(n,0,-1):
    print("*"*i)

'''
#  * * * * *
#   * * * *
#    * * *
#     * *
#      *
'''n=int(input("enter row:"))  
for i in range(n,0,-1):
    print(" "*(n-i)+" *"*i)'''
#      *
#     * *
#    * * *
#   * * * *
#  * * * * *
#   * * * *
#    * * *
#     * *
#      *
'''n=int(input("enter row:"))  
for i in range(1,n+1):
    print(" "*(n-i)+" *"*i)
m=n-1
for i in range(m,0,-1):
    print(" "*(n-i)+" *"*i)
'''
#     *
#    **
#   ***
#  ****
# *****
# *****
# ****
# ***
# **
# *
'''n=int(input("enter row:"))  
for i in range(1,n+1):
    print(" "*(n-i)+"*"*i)
for i in range(n,0,-1):
    print("*"*i+" "*(n-i))'''
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
'''n=int(input("enter row:"))  
for i in range(1,n+1):
    print("* "*i)
m=n-1
for i in range(m,0,-1):
    print("* "*i)
'''
#     *
#    **
#   ***
#  ****
# *****
# *****
#  ****
#   ***
#    **
#     *
'''n=int(input("enter row:"))  
for i in range(1,n+1):
    print(" "*(n-i)+"*"*i)
for i in range(n,0,-1):
    print(" "*(n-i)+"*"*i)'''

