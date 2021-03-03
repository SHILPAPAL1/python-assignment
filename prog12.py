#a power m

def power(a,m):
    k=1
    for i in range (0,m):
    #while(m>0):
        k=k*a
        #m=m-1
    return k

a=(int)(input("Enter a: "))
m=(int)(input("Enter m: "))
print(power(a,m))