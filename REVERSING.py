n=[]
x=int(input("enetr the elements you want to add: "))
for i in range(0,x):
    y=input("eneter the elements: ")
    n.append(y)
print(n)
n.reverse()
print(n)
a=n[4::-1]
print(a)