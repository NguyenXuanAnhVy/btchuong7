# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 16:09:40 2024

@author: anhvy 
"""
#a 
def tong_n(n):
    S = 0 
    for i in range(1, n+1):
        S += i
    return S
#b 
def tong_binh_phuong(n):
    S = 0
    for i in range(1 , n+1):
        S += i**2
    return S 
#c 
def tong_nghich_dao(n):
    S = 0
    for i in range(1, n+1):
        S += 1/i
    return S
#d
def tong_giai_thua(n):
    S = 0
    for i in range(1, n+1):
        giaithua = 1
        for j in range(1, i+1):
            giaithua *= j
        S += giaithua
    return S 
#e
def tich(n):
    S = 0
    for i in range(1, n+1):
        S *= i
    return S

if __name__ == "__main__":
    print(tong_n(2))
    print(tong_binh_phuong(5))
    print(tong_nghich_dao(3))
    print(tong_giai_thua(7))
    print(tich(9))
    