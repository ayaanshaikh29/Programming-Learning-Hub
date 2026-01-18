fruits = ["Mango", "Orange", "Apple", 7, 31.24, "Azaan", True]
print(fruits)

fruits.append("Azaan") # APPEND ADDING AT THE END
print(fruits) 


L1 = [12,25,47,84,65,11,0,35,45,21,66]
L1.sort() #SORTS LIST IN ASCENDING ORDER
print(L1)

L1.reverse() #REVERSE THE LIST 
print(L1)

L1.insert(8,69) #INSERTS 69 AT INDEX 8
print(L1)

L1.remove(69) #REMOVES ELEMENT 
print(L1)

L1.pop(5) #REMOVES ELEMENT FROM INDEX AND RETURN THE VALUE
print(L1)
print(L1.pop(5))


#TO PRINT VALUE WE CAN USE 
value = L1.pop(5)
print(value)

