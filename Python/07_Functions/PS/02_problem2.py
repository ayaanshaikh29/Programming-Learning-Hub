def c_to_f(c):
    return ((9*(c/5))+32)


c = float(input("Enter Temperature in Celsius: "))
C = c_to_f(c)
print(f"{C}°F")