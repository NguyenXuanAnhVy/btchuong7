# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 16:27:19 2024

@author: anhvy
"""
def fibonacci(n):
    fib = []
    a, b = 0, 1
    for i in range(n):
        fib.append(a)
        a, b = b, a+b
    return fib
if __name__=="__main__":
    print(fibonacci(6))
