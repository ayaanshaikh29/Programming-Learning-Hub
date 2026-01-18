def goodDay(name , ending="Thank You!!"):
    print(f"Good Day, {name}")
    print(ending)

goodDay("Ayaan") #here the default argument will work

goodDay("Azaan", "Thanks") #whereas here ending is given by the user itself so default won't work here