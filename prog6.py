#Check a number is prime palindrome or not.

def prime(num):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                return False
                break
        else:
            return True
    else:
        return False
    
def palindrome(num):
    copy=num
    r=0
    while(num>0):
        r=r*10+num%10
        num=num//10
    if (copy==r):
        return True
    else:
        return False

n=(int)(input("Enter a Number: "))
if prime(n) and palindrome(n):
    print("Yes")
else:
    print("No")