# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 21:47:08 2024

@author: anhvy 
"""
def kiemtra(n):
    if n<0 and n%2!=0:
        return -1
    elif n>0 and n%2==0:
        return 1
    else:
        return 0
if __name__=="__main__":
    print(kiemtra(5))
    
