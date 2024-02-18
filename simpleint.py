r=int(input("enter the principle"))
t=int(input("enter the rate"))
p=int(input("enter the time"))
def simple_interest(p,r,t):
    simple1_interest=p*r*t/100
    return simple1_interest
a=simple_interest(r,t,p)
print(a)
# def simple2():
#     g=p*r*t/100
#     return g
# c=simple2()
# print(c)
