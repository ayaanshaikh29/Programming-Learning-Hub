'''
Sum(1) = 1
Sum(2) = 1 + 2
Sum(3) = 1 + 2 + 3
Sum(4) = 1 + 2 + 3 + 4 
Sum(5) = 1 + 2 + 3 + 4 + 5

Sum(n) = 1 + 2 + 3 + 4 + ... + n-1 + n
sum(n) = sum(n-1) + n

'''
def sum(n):
    if(n==1):
        return 1
    return sum(n-1) + n

n = int(input("Enter a number: "))
print(f"The sum of numbers till {n} is: {sum(n)}")


