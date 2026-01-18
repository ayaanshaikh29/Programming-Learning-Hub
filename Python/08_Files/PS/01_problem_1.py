f = open("poem.txt")
content = f.read()

if("Twinkle" in content):
    print("The word Twinkle is in the file.")
else:
    print("The word Twinkle is not in the file.")

f.close() 