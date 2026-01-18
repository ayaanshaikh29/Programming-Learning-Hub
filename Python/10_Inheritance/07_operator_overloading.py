class Number:
    def __init__(self,n):
        self.n = n

#operators overloading:

    def __add__(self,num): #ADDITION
        return self.n + num.n
    
    def __sub__(self,num): #SUBSTRACTION
        return self.n - num.n
    
    def __mul__(self,num): #MULTIPLICTAON
        return self.n * num.n
    
    def __truediv__(self,num): #DIVISION
        return self.n / num.n
    
n = Number(10)
m = Number(5)

print(n+m)
print(n-m)
print(n*m)
print(n/m)