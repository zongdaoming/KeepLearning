#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @author: Naive Dorming
# @time: 2021/03/29 20:04:39

addresses = [
        "123 Elm Street",
        "123 Oak Street",
        "678 Elm Street"
        ]

user_address = input("Enter an address: ")
for address in addresses:
    if user_address.lower() in address.lower(): # Making the search case incencitive
        print(address)