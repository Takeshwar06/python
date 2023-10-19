# DocString --> documentation for another developer define usin: """this is doc""" 

# vaild doc string first in function body
def docString():
    """this is a doc string""" 
    return None

print(docString.__doc__) # carefully see docString is method but 

# if not in first in fucntion body then it is not vaild doc string it return None bydefault
def inVaildDocString():
    number=5
    """this is doc string"""
    return 5

print(inVaildDocString())
print(inVaildDocString.__doc__) # carefully see docString is method but 