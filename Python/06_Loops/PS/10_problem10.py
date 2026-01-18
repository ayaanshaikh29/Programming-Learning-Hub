'''
multiplication in reverse using while 1 10 (11)
n = int(input("Enter a number: "))    2 9 (11)
                                      3 8 (11)
print("Table of: ",n)                 4 7 (11)
                                      5 6 (11)
i = 10                                6 5 (11)
                                      7 4 (11)
while(i>=1):                          8 3 (11)
    print(f" {n} X {i} = {n*i} ")     9 2 (11)
    i -= 1                            10 1 (11)
'''

n = int(input("Enter a number: "))

for i in range(1,11):
    print(f"{n} X {11-i} = {n*(11-i)}")