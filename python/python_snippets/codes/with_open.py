#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @author: Naive Dorming
# @time: 2021/03/29 21:28:33

path = input("Please enter the path to a text file: ")
with open(path, 'r') as my_file: # 'r' means we are opening the file in read mode
	print(my_file.read())
