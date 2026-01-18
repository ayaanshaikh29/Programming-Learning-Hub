word = "donkey"

with open("file_4.txt") as f:
    content = f.read()

Newcontent = content.replace (word , "######")

with open("file_4.txt" , "w") as f:
    f.write(Newcontent)