#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @author: Naive Dorming
# @time: 2021/03/29 20:19:49

fabonacci = [1,1]
[fabonacci.append(fabonacci[i-1],fabonacci[i-2]) for i in range(2,100)]
print(fibonacci)

def fib():
    series =  [1,1]
    for i in range(2,100):
        prev_1 = series[i-1];
        prev_2 = series[i-2];
        new = prev_1 + prev_2;
        series.append(new);
    
    return series;

fabonacci = fib();
print(fabonacci)



def recur(n):
    if n == 0 or n == 1:
        return 1
    else:
        return (recur(n - 1) + recur(n - 2))

series = []
for i in range(100):
    number = recur(i)
    series.append(number)

print(series)
