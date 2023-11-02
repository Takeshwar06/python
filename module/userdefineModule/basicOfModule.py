# refere --> https://www.w3schools.com/python/python_modules.asp

# Consider a module to be the same as a code library.
# A file containing a set of functions you want to include in your application.

# To create a module just save the code you want in a file with the file extension .py

import module.userdefineModule.mymodule as mymodule # from local
# import mymodule as tiger  # if i need my own name 

a = mymodule.person1
print(a) #{'name': 'John', 'age': 36, 'country': 'Norway'}