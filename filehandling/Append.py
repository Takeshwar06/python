f = open("c:/Users/PC-ASUS/Desktop/python/filehandling/append.txt", "a")
f.write("Now the file has more hello!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())