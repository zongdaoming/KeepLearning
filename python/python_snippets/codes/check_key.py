#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @author: Naive Dorming
# @time: 2021/03/29 20:13:01

dictionary = {
    "fIRe": "combustion or burning, in which substances combine chemically with oxygen from the air and typically give out bright light, heat, and smoke.",

    "Wood": "the hard fibrous material that forms the main substance of the trunk or branches of a tree or shrub, used for fuel or timber.",
    
    "glaSS": "a hard, brittle substance, typically transparent or translucent, made by fusing sand with soda, lime, and sometimes other ingredients and cooling rapidly. It is used to make windows, drinking containers, and other articles."
}

users_key = input("Endter a key here: ")
users_key = users_key.lower()

found = False # Using a boolean variable to check whether the key exist or not

for key in dictionary:
    if key.lower() == users_key:
        found = True
        print(dictionary[key])

if found is not True:
    print("The key doesn't exist in the dictionary")


# 
key = input("Enter a key here: ")
print(dictionary.get(key.lower()))

# 
key = input("Enter a key here: ")
key = key.lower()

try:
    print(dictionary[key.lower()])
except:
    print(f"Sorry the key {key} doesn't exist in the dictionary")
