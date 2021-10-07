 # Project Name:: Pattern printing in python

print("For how many rows you want to draw your pattern::")
n = int(input())
print("Enter 1 or 0 for printing respective pattern::", end="")
d = int(input())
c = bool(d)
if c==False:
    for i in range (0,n):
        for j in range (0,i+1):
            print("*",end=" ")
        print("")
elif c==True:
    for i in range (n,0,-1):
        for j in range (0,i):
            print("*",end=" ")
        print("")
