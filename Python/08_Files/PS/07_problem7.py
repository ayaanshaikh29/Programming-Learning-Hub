with open("log.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if ("python" in line):
        print(f"Yes Python is in the file. At line {lineno}")
        break # by adding break the for`` loop will only find python once in the
              # first line if we have to find it for   
              # the other lines too then dont break the loop
    lineno += 1

else:
    print("Yes Python is not in the file.")