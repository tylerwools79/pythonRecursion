import math

#creates a sliding window structure, shows in and out
def recWindow(n,max):
    print()
    for i in range(n):
        print(' ',end = '')
    for i in range(max-n):
        print("*",end='')
    if n == max:#base case
        print()
        return
    else:
        recWindow(n+1,max)
    for i in range(max - n):
        print("*", end='')
    for i in range(n):
        print(' ',end = '')
    print()

#creates a diamond structure, shows in and out
def recDiamond(n,max):
    for i in range(math.ceil((max-n)/2)):
        print(' ',end = '')
    for i in range(n):
        print("*",end = '')
    if(n>=max):#base case
        print()
        return
    else:
        print()
        recDiamond(n+2,max)
    for i in range(math.ceil((max-n)/2)):
        print(' ',end = '')
    for i in range(n):
        print("*",end = '')
    print()

#makes a steplike structure in and out
def recSteps(n):
    for i in range (n):
        print('*',end='')
    print()
    if(n <= 0):#base case
        print()
        return
    recSteps(n-1)
    for i in range (n):
        print('*',end='')
    print()

#makes a pyramid
def recPyr(c,max):
    for i in range(math.ceil((max-c)/2)):
        print(' ',end='')
    for i in range(c):
        print('*',end='')
    print()
    if(c>=max):#base case
        return
    else:
        recPyr(c+2,max)


#demonstrates a mathematical recursion, each number is the previous number doubled
def recMath(n,level):
    if(n>=33):
        print("level:",level,"n: ",n)
        return n
    print("level:",level,"n: ",n)
    recMath(n+n,level+1)
    print("level:", level, "n: ", n)
    return n


print()
recWindow(0,5)
print()
recDiamond(1,10)
print()
recSteps(10)
print()
recPyr(1,10)
print()
recMath(1,0)
print()