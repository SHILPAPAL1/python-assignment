#Count the number of non-zero digits in the number

a=(int)(input("Enter the number: "))
c=0
while(a>0):
    if (a%10!=0):
        c=c+1
    a=a//10
print("Number of non-zero digits in a number are: ",c)