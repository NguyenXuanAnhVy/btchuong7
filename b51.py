# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 21:49:45 2024

@author: anhvy
"""
def ktra_gtri():
    gtri = input("Nhap gia tri:")
    #if gtri.replace('.','',1).replace('-','',1).isdigit():
        #gtri = float(gtri)
    #cach 2 kiem tra, ep kieu int()
    #if gtri.lstrip('-').isdigit()
        #gtri= int(gtri)
    #vi du: -12344-, cat dau tru truoc va sau 
    if gtri.strip('-').isdigit():
        gtri = int(gtri)
    if -86 <= gtri <= 90:
        return gtri
    print("Khong hop le, nhap lai:")
    return ktra_gtri()
if __name__=="__main__":
    print(ktra_gtri())
    

