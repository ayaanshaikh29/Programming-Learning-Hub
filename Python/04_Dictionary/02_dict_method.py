marks = {
    "Ayaan": 95,
    "Azaan": 98,
    "Armaan":96,
    10:"Hasan"
}

print(marks.items()) #PRINTS ALL ITEMS IN A LIST FORM
print(len(marks)) #PRINTS LENGTH OF DICTIONARY
print(marks.keys()) #IT PRINTS KEY PAIRS IN LIST FORM

print(marks.values()) #IT PRINTS VALUE PAIRS IN LIST FORM 

marks.update({97:"Hasan","Ahlam":99}) #IT UPDATES THE DICTIONARY AS IT IS MUTABLE
print(marks)

print(marks.get("Ayaan")) #MARKS OF AYAAN
print(marks.get("Ayaan2")) #IT GIVES NONE SIVE AYAAN2 IS NOT IN THE DICT
print(marks["Ayaan2"]) #IT GIVES AN ERROR

