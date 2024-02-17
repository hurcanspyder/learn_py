# temp=int(input("enter the temperature in celsius "))
# def temp_conv():
#     f=temp*9/5+32
#     return f
# x=temp_conv()
# print(x)

#PARAMETER USEd
temp=int(input("enter the temperature in celsius "))
def temp2_conv(cel:int)-> float:
    f=cel*9/5+32
    return f
x=temp2_conv(temp)
