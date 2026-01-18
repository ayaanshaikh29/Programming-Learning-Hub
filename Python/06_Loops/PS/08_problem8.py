'''
for n = 3
(stars i.e 1,2,3) for this we will use for which "*" X i and i is from 1 to n+1(n=n-1;n+1=n+1-1)
for spaces we will keep it either empty or multiply by 1
* (2*1-1),spaces = 3-1
** (2*2-1),spaces = 3-2
*** (2*3-1),spaces = 3-3
'''

n = int(input("Enter a number:"))
for i in range(1,n+1): #agar n rakhega ton n-1 tak print hoga 
#n+1 rakh toh woh n+1-1=n tak print hoga
    print(" ",end="") #ye statement add nahi kiye toh bhi chalega
    print("*"*(i),end="")
    print("")
