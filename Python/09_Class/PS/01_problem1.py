class programmer:
    company = "Microsoft"

    def __init__(self,name,salary,city):
        self.name = name 
        self.salary = salary
        self.city = city 

p1 = programmer("Ayaan", 1200000, "Navi Mumbai")
print(p1.name,p1.company,p1.salary,p1.city)

p2 = programmer("Azaan", 2400000, "Navi mumbai")
print(p2.name,p2.company,p2.salary,p2.city)

p3 = programmer("Armaan", 2000000, "Mumbai")
print(p3.name,p3.company,p3.salary,p3.city)