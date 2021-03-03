#GCD of 2 numbers

def compute_gcd(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            gcd = i 
    return gcd

num1 = (int)(input("Enter the first number: "))
num2 = (int)(input("Enter the second number: "))

print("The GCD is", compute_gcd(num1, num2))