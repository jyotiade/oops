A1=str(input("enter school name="))
B1=int(input("enter Roll no ="))
C1=str(input("enter center name="))
D1=int(input("enter  school code="))
E1=str(input("enter  name="))
F1=str(input("enter father name="))
G1=str(input("enter mother name="))
H1=int(input("enter class name="))
I1=str(input("enter dob="))
J1=int(input("enter hindi mark="))
K1=int(input("enter  english mark="))
L1=int(input("enter maths mark="))
M1=int(input("enter  sanskrit mark="))
N1=int(input("enter sceince mark="))

print("\t\tBOARD OF SECONDARY EDUCATION,M.P BHOPAL")
print("\tHIGH SECONDARY EXAMINATION 10 2003,M.P ,BHOPAL")
print("\nSchool:",A1,end="")
print("\n\nRoll no:",B1,"\t\t\t\tCenter:",C1,end="")
print("\n\nName:",E1,"\t\t\t\tSchool code:",D1,end="")
print("\n\nfather name:",F1,"\t\t\t\tClass",H1,end="")
print("\n\nmother name:",B1,"\t\t\t\tDOB:",I1,end="")

print("\n\n\tSub Code      sub Name       Max      Min        Obtain")
print("\n\n\tH001          hindi          100      33    ",J1)
print("\n\n\tE001          english        100      33    ",K1)
print("\n\n\tM001          maths          100      33    ",L1)
print("\n\n\tSA001         sanskrit       100      33    ",M1)
print("\n\n\tS001          science        100      33    ",N1)


if J1<0 or J1>100:
    print("invalid")
elif K1<0 or  K1>100:
    print("invalid")
elif L1<0 or  L1>100:
    print("invalid")
elif M1<0 or  M1>100:
    print("invalid")
elif N1<0 or  N1>100:
    print("invalid")

    

total=J1+K1+L1+M1+N1
per=total/5

print("total mark:",total)
print("per:",per)

if per>=80:
    print("first division")
elif per>=60:
    print("second division")
elif per>=40:
    print("third division")
else:
    print("fail")