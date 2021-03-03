#Display twin-prime numbers within a range
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

a=(int)(input("Enter the first number: "))
b=(int)(input("Enter the second number: "))
for i in range (a,b-2):
    if (prime(i) and prime(i+2)):
        print("(",i,", ",(i+2),"), ")