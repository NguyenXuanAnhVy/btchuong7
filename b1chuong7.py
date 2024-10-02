# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 19:49:25 2024

@author: anhvy
"""
import math

# Ham tinh can bac n tu mot so thuc
def can_bac_n(x, n):
    if n <= 0:
        return "n phai lon hon 0"
    return x ** (1/n)

# Ham tinh gia tri binh phuong cua mot so duong
def binh_phuong(x):
    if x <= 0:
        return "x phai la so duong"
    return x ** 2

# Ham kiem tra mot so nhap vao la so chan co gia tri am
def kiem_tra_chan_am(x):
    return x < 0 and x % 2 == 0

# Ham kiem tra mot so nhap vao
def kiem_tra_so(x):
    if x < 0 and x % 2 != 0:
        return -1  # So am le
    elif x > 0 and x % 2 == 0:
        return 1   # So duong chan
    else:
        return 0   # Truong hop khac

# Ham kiem tra gia tri nhap vao thuoc đoan [-89, 90]
def kiem_tra_gia_tri(x):
    while x < -89 or x > 90:
        x = float(input("Gia tri nhap vao khong hop le. Vui long nhap lai: "))
    return x

# Vi du su dung
if __name__ == "__main__":
    # Kiểm tra hàm
    print("Can bac 3 cua 27:", can_bac_n(27, 3))
    print("Binh phuong cua 5:", binh_phuong(5))
    print("Kiem tra -4:", kiem_tra_chan_am(-4))
    print("Kiem tra -3:", kiem_tra_so(-3))
    print("Kiem tra 4:", kiem_tra_so(4))
    
    # Nhập giá trị
    x = float(input("Nhap mot gia tri trong khoang [-89, 90]: "))
    x = kiem_tra_gia_tri(x)
    print("Gia tri hop le:", x)