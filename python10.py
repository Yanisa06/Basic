"""
#
# Part: Python JSON
# API = Application Programing Interface
#
"""
import json

# make a json (String)
x ='{"name": "JSON", "age": 20, "city": Phuket"}'
print(x)

# prase
y = json.loads(x)

# python dictionary
print(y)
print(type(y))
print(y["city"])

# python dicionary
a = {
    "name" : "Noa"
    "age" : 20,
    "city" : "Phuket",
}

# convert to JSON (String)
b = json.dumps(a)

# JSON String
print(b)
