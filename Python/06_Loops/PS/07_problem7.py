'''
for n = 3
(odd stars i.e 1,3,5) for this we will use 2*i-1 for which i is 1 to n+1(n=n-1,n+1=n+1-1)
for spaces n-i
  * (2*1-1),spaces = 3-1
 *** (2*2-1),spaces = 3-2
***** (2*3-1),spaces = 3-3

for n = 5
    * (2*1-1),spaces = 5-1
   *** (2*2-1),spaces = 5-2
  ***** (2*3-1),spaces = 5-3
 ******* (2*4-1),spaces = 5-4
********* (2*5-1),spaces = 5-5

'''

n = int(input("Enter a number:"))
for i in range(1,n+1): #agar n rakhega ton n-1 tak print hoga 
#n+1 rakh toh woh n+1-1=n tak print hoga
    print(" "*(n-i),end="")
    print("*"*((2*i)-1),end="") #odd stars printing mechanism
    print("")
