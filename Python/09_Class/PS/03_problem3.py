class demo:
    a = 4 # class attribute 

o = demo()
print (o.a) #here the class attribute is set hence it will get print 

o.a = 0 # instance attribute
print (o.a) #as here we have an instance attribute so the class attribute
#will not get set whereas the instance will get set
''' this shows that the class attribute doesnt get change only because 
of instance it gets replace '''