# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 12:37:00 2024

@author: anhvy 
"""
import math
def chuvi_dt(hinh, pheptinh, *args, **kwargs):
    if hinh == 'vuong':
       canh = args[0]
       return canh*4 if pheptinh == 'chuvi' else canh**2
    elif hinh == 'chunhat':
        dai = args[0]
        rong = args[1]
        return 2*(dai+rong) if pheptinh == 'chuvi' else dai*rong
    elif hinh == 'tron':
        bk = args[0]
        return 2*bk*math.pi if pheptinh == 'chuvi' else bk**2*math.pi
    else:
        return "Hinh khong dung."
if __name__=="__main__":
    print("Chu vi hinh vuong:", chuvi_dt('vuong', 'chuvi',5))
    print("Dien tich hinh vuong:", chuvi_dt('vuong', 'dientich',5))
    print('Chu vi hinh chu nhat: ', chuvi_dt('chunhat','chuvi', 5, 4))
    print('Dien tich hinh chu nhat: ', chuvi_dt('chunhat','dientich', 5, 4))
    print('Chu vi hinh tron:', chuvi_dt('hinhtron','chuvi', 5))
    print('Dien tich hinh tron: ',chuvi_dt('hinhtron','dientich',5))
    