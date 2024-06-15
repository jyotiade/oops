
#==============================range=======================================


# x=range(-1,-11,-1)
# print(x)
# print(list(x))
# print(tuple(x))
'''output:
range(-1, -11, -1)
[-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
(-1, -2, -3, -4, -5, -6, -7, -8, -9, -10)'''

# x=range(1,11,-1)
# print(x)
# print(list(x))
# print(tuple(x))
'''output:
range(1, 11, -1)
[]
()
'''
# x=range(1,11,1)
# print(x)
# print(list(x))
# print(tuple(x))
'''output:
range(1, 11)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)'''

# NOTE:
# (end-1)=positive direction   ====>range(start,stop[end-1])
# (end+1)=negative direction   ====>range(start,stop[end+1])