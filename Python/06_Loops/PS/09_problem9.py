'''
***
* *    for n=3
***
'''
# end="" do ya usse zyada print statement ko combine karta hai 
n = int(input("Enter a number: "))

for i in range(1,n+1):
    if(i==1 or i==n):
        print("*" * n ,end="") 
    else:
        print("*" ,end="")
        print(" " * (n-2) ,end="")
        print("*" ,end="")
    print("")