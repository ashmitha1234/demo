a=int(input("Enter the first number : "))
b=int(input("Enter the second number : "))
c=int(input("Enter the third number : "))
if((a>b) & (a>c) & (b>c)):
    print(a,"is the maximum number and",c,"is the minimum number")
elif((a>b) & (a>c) & (c>b)):
    print(a,"is the maximum number and",b,"is the minimum number")
elif((b>a) & (b>c) & (a>c)):
    print(b,"is the maximum number and",c,"is the minimum number") 
elif((b>a) & (b>c) & (c>a)):
    print(b,"is the maximum number and",a,"is the minimum number")
elif((c>a) & (c>b) & (a>b)):
    print(c,"is the maximum number and",b,"is the minimum number")
else:
    print(c,"is the maximum number and",a,"is the minimum number")
