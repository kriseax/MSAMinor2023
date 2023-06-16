#declare variables
a = 7
b = 14
c = 11

#determine which is largest a, b, or c
if a > b:
    #compare a to c
    if a > c:
        print("A is largest")
    else:
        print("C is largest")
else:
    #compare b to c
    if b > c:
        print("B is largest")
    else:
        print("C is largest")

#Optimized Code
#if a > b and a > c. A is the largest
#if b > a and b > c. B is the largest
#else C is the largest

if (a > b) and (a > c):
    print("A is the largest")
elif (b > a) and (b > c):
    print("B is the largest")
else:
    print("C is the largest")



if (a > b) and (a > c):
    print("A is the largest")

if (b > a) and (b > c):
    print("B is the largest")

if(c > a) and (c > b):
    print("C is the largest")
