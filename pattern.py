# *
# **
# ***
# ****
# *****
'''n=int(input("enter no="))
i=1
while i<=n:
    print(i*'*')
    i=i+1

'''
#     *
#    **
#   ***
#  ****
# *****
'''n=int(input("enter no="))
i=1
while i<=n:
    print((n-i)*' '+ i*'*')
    i=i+1
'''

#      *
#     * *
#    * * *
#   * * * *
#  * * * * *
'''n=int(input("enter no="))
i=1
while i<=n:
    print((n-i)*' '+i*'* ')
    i=i+1'''

#     *
#    ***
#   *****
#  *******
# *********

'''n=int(input("enter no="))
i=1
while i<=n:
    print((n-i)*' '+(2*i-1)*'*')   #odd no (2*n-1)
    i=i+1

'''
# *****
# ****
# ***
# **
# *
'''n=int(input("enter no="))
i=n
while i>=0:
    print(i*'*')
    i=i-1
'''

# *****
#  ****
#   ***
#    **
#     *

'''n=int(input("enter no="))
i=n
while i>=0:
    print((n-i)*' '+ i*'*')
    i=i-1'''


#  * * * * *
#   * * * *
#    * * *
#     * *
#      *
'''n=int(input("enter no="))
i=n
while i>=0:
    print((n-i)*' '+i*' *')
    i=i-1
'''

# *********
#  *******
#   *****
#    ***
#     *
'''n=int(input("enter no="))
i=n
while i>=0:
    print((n-i)*' '+(2*i-1)*'*')   #odd no (2*n-1)
    i=i-1'''


# *****
#  ****
#   ***
#    **
#     *
'''n=int(input("enter no="))
i=0
while i<n:
    print(i*' '+(n-i)*'*')       #when i start with 0 not with n ,reverse order
    i=i+1'''

'''*
**
***
****
*****
****
***
**
*'''

# n=int(input("enter no="))
# i=1
# while i<n:
#     print(i*'*')
#     i=i+1
# i=n
# while i>=0:
#     print(i*'*')
#     i=i-1

