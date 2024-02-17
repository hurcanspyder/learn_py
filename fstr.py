#string formating 
#method 1
a=100
b = f"value of a is {a}"
print(b)
#method 2 
letter="hey my name is {} and iam from {}"
country="india"
name="abhishek"
print(letter.format(name,country))
#if we are using 1 and 0 here{} it we can the order of arguments normaly first value correspond  to first bracket
# method 2.2 


letter="hey my name is {} and iam from {}"
country="india"
name="abhishek"
print(letter.format(name,country))


txt="my marks is {marks:.2f}"     #we are using 2 here because we are taking value upto 2 decimal places
marks=78.666
print(txt.format(marks=marks))

