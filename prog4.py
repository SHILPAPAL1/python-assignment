#Display non-fibonacci no. within a range

a=(int)(input("Enter the first number: "))
n=(int)(input("Enter the second number: "))
b=1
c=0
while (c<=n):
    c=a+b
    a=b
    b=c
    d=a+b
    for x in range (c+1,d):
        if x<=n:
            print(x," ")
        else:
            break