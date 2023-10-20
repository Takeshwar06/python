# break statment directly skip the loop 
print("break key word")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

# constinue statment skip only one iteration 
print("continue key word")
for x in fruits:
  if x=="banana":
    continue
  print(x)