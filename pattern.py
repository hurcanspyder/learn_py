def pattern (n):
    for i in range(0,n+1):          # for rows 
        for j in range(0,i):        # for columns
            print(".",end=" ")

        for s in range(n-i,0,-1):   # for columns
            print("*",end=" ")
        print()

pattern (5)
    