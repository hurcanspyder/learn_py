n=5
for i in range(0,n+1):
    for k in range(n-i,0,-1):
        print(" ",end=(" "))
    for s in range(0,i):
        print("*",end=(" "))
    
    for s in range(1,i):
        print("*",end=(" "))
    print()
    