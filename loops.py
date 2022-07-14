import pymongo
print("-----------WHILE LOOPS----------------")

i=0
while i<5:
    print(i)
    i=i+1

print("------------For Loop------------")
for item in range(6):
    print(item)

print("---------NESTED FOR LOOP---------")
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)