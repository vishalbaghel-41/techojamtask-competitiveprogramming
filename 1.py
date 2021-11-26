x=int(input("Enter a number:"))
s=x
k=int(input("enter a constant"))
if x%10 != 0:
    for i in range(0,k-1):
        if x%10 != 0:
            x=x-1
        if x%10 == 0:
            x=x/10
    print(x)
if s%10 == 0:
    for i in range(0,k):
        if s%10 != 0:
            s=s-1
        if s%10 == 0:
            s=s/10   
    print(s) 
