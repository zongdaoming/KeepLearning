#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @author: Naive Dorming
# @time: 2021/03/29 20:17:12

number = int(input("Enter a number >>> "))
if int((number**2)**0.5) == number: # The number is postive
    print('+' * number)
else: # The number is negative
    print('-' * (-1 * number)) 

