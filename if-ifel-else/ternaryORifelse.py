
# if elif else

a,b=1005,105
if a!=b:
    if a>b:
        print("a is greater")
    else:
        print("b is greater")
else:
    print("both are equal")


# ternary operator 
print("both are equal" if a==b else "a is greater" if a>b else "b is greater")
# print("tiger "*4) # for time repeat the string 