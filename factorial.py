n = int(input("enter your number:- "))
f = 1
if n<0:
    print("not exit " )
elif n==0:
    print("The factorial  0 is 1")
else:
    for i in range(1,n+1):
        f=f*i
    print("Factorial  ",n," is ",f)
