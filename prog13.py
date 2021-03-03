#Calculate factor of a number.

n = int(input("Enter any number: "))
for i in range(1, n):
    if(n % i == 0):
        print(i)