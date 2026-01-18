words = ["donkey" ,"hate" ,"gande"]

with open("file_4.txt") as f:
    content = f.read()

for word in words:
    content = content.replace (word , "#" * len(word))

with open("file_4.txt" , "w") as f:
    f.write(content)