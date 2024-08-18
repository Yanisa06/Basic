"""
#
# Part : Python collection
# List, Table, set and Dictionary
#
"""

"""
#
# Part: Python List
#
"""
this_list= ["apple", "banana", "coconat", "apple", "banana"]
print(this_list)
print(type(this_list))
print(len(this_list))

print(this_list[2])

this_list.append("cherry")
print(this_list, len(this_list))
this_list.insert(1, "orange")
print(this_list, len(this_list))

this_list2 = ["apple", "banana", "coconat", "apple", "banana"]
this_list3 = ["mango", "pineapple", "grape"]
this_list2.extend(this_list2)
print(this_list2, len(this_list2))

this_list4 = ["apple", "banana", "coconat", "apple", "banana"]
this_list4.remove("banana")
print(this_list4, len(this_list4))

this_list5 = ["apple", "banana", "coconat", "apple", "banana"]
this_list5.pop(2)
print(this_list5, len(this_list5))

this_list6 = ["apple", "banana", "coconat", "apple", "banana"]
del this_list6[1]
print(this_list6, len(this_list6))

this_list6.clear()
print(this_list6, len(this_list6))

del this_list
# print(this_list5, Len(this_list5))

this_list7 = ["orange", "mango", "kiwi", "pineapple", "banana"]
this_list7.sort()
print(this_list7, len(this_list7))

this_list8 = ["orange", "mango", "kiwi", "pineapple", "banana"]
this_list8.reverse()
print(this_list8, len(this_list8))

List1 = ["a", "b", "c"]
List2 = [1, 2, 3]
List3 = List = List2
print(List3)

"""
#
# Part: python Tuple
#
"""
This_tuple = ("apple", "banana", "coconat")
print(This_tuple)
print(type)
print(len(This_tuple))

print(This_tuple[0])

This_tuple2 = ("apple", "banana", "coconat")
This_tuple3_list = list(This_tuple2)
print(This_tuple3_list, type(This_tuple3_list))
This_tuple4 = tuple(This_tuple3_list)
print(This_tuple4, type(This_tuple4))

This_tuple5 = ("apple", "banana", "coconut")
This_tuple6_list = list(This_tuple5)
This_tuple6_list.append("durian")
This_tuple7 = tuple(This_tuple6_list)
print(This_tuple7, type(This_tuple7))

This_tuple8 = ("apple", "banana", "coconut")
This_tuple9_list = list(This_tuple8)
This_tuple9_list.remove("banana")
This_tuple8 = tuple(This_tuple9_list)
print(This_tuple8, type(This_tuple8))

del This_tuple8
# print(this_tuple8, type(this_tuple8))

Tuple1 = ("a", "b", "c")
Tuple2 = (1, 2, 3)
tuple3 = Tuple1 + Tuple2
print(tuple3, type(tuple3))

"""
#
# Part: Python Tuple
#
"""
this_set = {"apple", "banana", "coconut"}
print(this_set)
print(type(this_set))
print(len(this_set))

for x in this_set:
    print(x)

print("banana" in this_set)

this_set2 = {"apple", "banana", "coconut"}
this_set2.add("durian")
print(this_set2, type(this_set2))
this_set2.remove("coconut")
print(this_set2, type(this_set2))

this_set3 = {"apple", "banana", "coconut"}
this_set4 = {"durain", "grape"}
this_set3.update(this_set4)
print(this_set3, type(this_set3))

# union (Euler)
this_set5 = {"apple", "banana", "coconut"}
this_set6 = {"durain", "grape"}
this_set7 = {1, 2, 3}
this_set8 = this_set5 | this_set6 | this_set7
print(this_set8, type(this_set8))

this_set8.clear()
print(this_set8, type(this_set8))
del this_set8
# print(this_set8, type(this_set8))

"""
#
# Part: Prthon Dictionary
#
"""
this_dict = {
    "brand": "Ford",
    "model": "Raptor",
    "year": "2024"
}
print(this_dict)
print(type(this_dict))
print(len(this_dict))

print(this_dict["brand"])
print(this_dict.get("year"))
print(this_dict.keys())

this_dict["year"] = "1987"
print(this_dict)
this_dict.update({
    "year": "1989",
    "model": "Mustang"
})
print(this_dict)

print(this_dict)

this_dict["color"] = "red"
print(this_dict)

del this_dict["year"]
print(this_dict)


this_dict.clear()
print(this_dict, type(this_dict))
del this_dict
# print(this_dict, type (this_dict))

this_dict2 = {
    "brand": "Toyota",
    "model": "Yaris",
    "year": "2016"
}

this_dict3 = {
    "brand": "Honda",
    "model": "civic",
    "year": "2024"
}

this_dict4 = {
    "brand": "Lamborghini",
    "model": "Huracan",
    "year": "2019"
}

my_car = {
    "car1": this_dict2,
    "car2": this_dict3,
    "car3": this_dict4
}
print(my_car, len(my_car))
print(my_car["car2"]["model"])




























"""
#
# Part Python Dictionary
#
"""
this_dict = {
    "brand": "Ford",
    "madel": "Rapter",
    "year": "2024"
}
print(this_dict)
print(type(this_dict))
print(len)


