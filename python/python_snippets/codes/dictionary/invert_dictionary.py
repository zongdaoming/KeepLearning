#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @author: Naive Dorming
# @time: 2021/03/30 02:14:37


# 实例方法只能被实例对象调用(Python3 中，如果类调用实例方法，需要显示的传self, 也就是实例对象自己)，静态方法(由@staticmethod装饰的方法)、类方法(由@classmethod装饰的方法)，可以被类或类的实例对象调用。

# 实例方法，第一个参数必须要默认传实例对象，一般习惯用self。
# 静态方法，参数没有要求。
# 类方法，第一个参数必须要默认传类，一般习惯用cls。

from collections import defaultdict
class Test(object):
    def __init__(self,title):
        super(Test, self).__init__()
        self.title = title

        self.my_dict = {
        'Izuku Midoriya': 'One for All', 
        'Katsuki Bakugo': 'Explosion', 
        'All Might': 'One for All', 
        'Ochaco Uraraka': 'Zero Gravity'
        }
        self.my_inverted_dict = {
        'One for All': ['Izuku Midoriya', 'All Might'], 
        'Explosion': ['Katsuki Bakugo'], 
        'Ochaco Uraraka': ['Zero Gravity']
        }
        # self.map_and_reversed()
        # self.zip_dict()
        self.default_dict()

    @staticmethod
    def printDict(**kwargs):
        """Print Keys and Vlaues of A Dictionary
        """
        for key, value in kwargs.items():
            print(f"key is {key}, value is {value}")

    @staticmethod
    def printf(dictionary):
        # 静态方法需要写上类的名字
        return Test.printDict(**dictionary)

    @classmethod
    def create(cls,title):
        obj = cls(title=title)
        return obj
    
    # Invert a Dictionary with Map and Reversed
    # dict or list + map(lambda:,iterable)

    def map_and_reversed(self):
        my_inverted_dict = dict(map(reversed, self.my_dict.items()))
        self.printf(my_inverted_dict)


    # Invert a Dictionary With zip
    def zip_dict(self):
        my_inverted_dict = dict(zip(self.my_dict.values(),self.my_dict.keys()))
        self.printf(my_inverted_dict)
    
    # Invert a Dictionary with a Comprhension
    def comprehension_dict(self):
        my_inverted_dict = {value:key for key,value in self.my_dict.items()}
        self.printf(my_inverted_dict)
    
    # Invert a Dictionary with Defaultdict
    def default_dict(self):
        my_inverted_dict = defaultdict(list)
        {my_inverted_dict[value].append(key) for key, value in self.my_dict.items()}
        self.printf(my_inverted_dict)
    
    # Invert a Dictionary with a For Loop
    def for_loop_set_default(self):
        my_inverted_dict = dict()
        for key,value in self.my_dict.items():
            my_inverted_dict.setdefault(value,list()).append(key)
        self.printf(my_inverted_dict)

    # Revert the Inversion
    def revert_inversion(self):
        my_dict = {value:key for key in self.my_inverted_dict for value in self.my_inverted_dict[key]}
        self.printf(my_dict)

