# To delete a file, you must import the OS module, and run its os.remove() function:
# first make TempFile.txt and do practical
import os
if os.path.exists("c:/Users/PC-ASUS/Desktop/python/filehandling/TempFile.txt"):
  os.remove("c:/Users/PC-ASUS/Desktop/python/filehandling/TempFile.txt")
  print("deleted")
else:
  print("The file does not exist")