# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 16:51:58 2024

@author: anhvy
"""
def tinh_chu_vi(a, b):
    return 2*(a+b)
def tinh_dien_tich(a, b):
    return a*b
def ve_hinh_chu_nhat(a, b):
    for i in range(b):
        print('*' * a)
if __name__=="__main__":
    print(tinh_chu_vi(2, 5))
    print(tinh_dien_tich(6, 8))
    print(ve_hinh_chu_nhat(2, 3))