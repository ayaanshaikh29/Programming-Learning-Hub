with open("log.txt") as f:
    content = f.read()

if ("python" in content):
    print("Yes Python is in the file.")
else:
    print("Yes Python is not in the file.")