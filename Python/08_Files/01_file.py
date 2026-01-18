'''
we have created a file named file.txt and now we have assigned a variable a that will 
open the file and we have also use an another variable data that will read the file 
and finally we print the data and close the file
'''
a = open("file.txt")
data = a.read() 
print(data)
a.close