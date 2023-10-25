# before 3.6
string="hello i am {1} and i am also a {0}"
print(string)
print(string.format("tiger","full stack developer"))


# after 3.6
name,profession="tiger","full stack developer"
# without "f" actual string print not populate name and profession
string=f"hello i am {name} and i am also a {profession}" 
string=f"{{name}} and {{profession}}" #actual string print not populate name and profession
print(string)