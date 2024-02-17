def add1():
    o=0
    for i in u:
        o=sum(u)
    return o
    
def sub1():
    if l==2:
        b=0
        for i in u:
            b=u[1]-u[0]
    else:
        print("you entered more then two digits")    
    return b

def multiply1():
    
    c=u[0]*u[1]*u[2]
    
    return c
def divide1():
    if l==2:
        k=u[1]/u[0]
    else:
        print("you entered more then two values")
    
    return k


while True:
    print("1.add \n2.subtract \n3.multiply \n4.divide \n5.exit ")
    x=int(input("enter the operator you want to use "))
    l=int(input("enter the integers you want to calculate: "))
    
    
    u=[]
    for i in range(0,l):
        y=int(input("enter the numbers:"))
        u.append(y)
    for i in (0,x):
        if x==1:
            v=add1()
            print(v)
        elif x==2:
            j=sub1()
            print(j)
        elif x==3:
            t=multiply1()
            print(t)
        elif x==4:
            a=divide1()
            print(a)
        
        elif x>=5:
            exit()
    print("THANKYOU MANOOOO........")
        
