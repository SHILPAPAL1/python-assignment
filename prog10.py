#Check whether a number is palindrome or not.

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
    
n=121
if palindrome(n):
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")