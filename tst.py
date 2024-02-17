#wap to o airthmatics operation with loop
def add1():
    x=num1+num2
    return x
def sub1():
    y=num1-num2
    return y
def div1():
    z=num1/num2
    return z
def exit1():
    exit()


while True:
    num1=int(input("enter the no."))
    num2=int(input("enter the no."))
    print("1.to add no.\n2.to subtract no. \n3.to divide no. \n4.to exit")
    x=int(input("enter the operator"))
    if x==1:
        a=add1()
        print(a)
    elif x==2:
        b=sub1()
        print(b)
    elif x==3:
        c=div1()
        print(c)
    elif x==4:
        exit1()
    print(" ...................................")
        
        
        


