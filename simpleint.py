p=int(input("enter the principle"))
r=int(input("enter the rate"))
t=int(input("enter the time"))
def simple_interest(p,r,t):
    simple1_interest=p*r*t/100
    return simple1_interest
a=simple_interest(p,r,t)
print(a)
