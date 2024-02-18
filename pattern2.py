def new_func():
    n=5
    for i in range(1,n+1):
        for k in range(n-i,0,-1):
            print(" ",end=(" "))
        for s in range(0,i*2-1):
            print("*",end=(" "))
        print()
    for g in range(1,n+1):
        for j in range(0,g):
            print(" ",end=(" "))
        for u in range(n-g,0,-1):
            print("*",end=(" "))
        for u in range(n-g-1,0,-1):
            print("*",end=(" "))
    
        print()

new_func()