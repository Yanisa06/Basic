"""
#
# Prat: Python while Loop
#
"""
i = 1
while i < 5:
    print("i = ", i)
    i+=1 # i = i + 1

   i = 1
   while i < 5:
    print("1 = ", i) 
    if i == 3:
        break
    i+=1 # i = i + 1    

# i = 1
#  while i < 5:
#    print("1 = ", i) 
#    if i == 3:
#        continue
#   i+=1 # i = i + 1 

i = 1
while i < 5:
    print("i = ", i)    
    i+=1 # i = i + 1
else:
    print("Game Over!")    

"""
#
# Part: Python For Loop
#
"""
fruits = ["apple", "banana", "coconut"]
for fruit in fruits:
    print("Fruit: ",fruit)

 for fruit in fruits:
    print("Fruit: ",fruit)   
    if fruit == "banana":
        break

for fruit in fruits:
    if fruit == "banana": 
        break
    print("Fruit: ",fruit)   
    
for fruit in fruits:
    if fruit == "banana": 
        continue
    print("Fruit: ",fruit) 

for x in range(len(fruits)):   
    print("Number: ", x)

for x in range(5):  
    print("Number: ", x)
    else:
    print("Game Over!")    

adjs = ["red", "brue", "green"]
fruits = ["apple", "banana", "coconut"]
for adjs in adjs:
    for fruit in fruits:  
        print("Fruit: " + adjs + " " + fruit)
       


          