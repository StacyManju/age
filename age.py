# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 21:03:24 2022

@author: jenny
"""
driving = input ('請問您開過車嗎? 有/沒有 ')
age = int(input('請輸入您的年齡: '))

if driving == '有':
    if age >=20:
        print('您確實可以開車')
    else:
        print('您的年齡還不能開車，請在確認一次您的年齡是否輸入正確')
elif driving == '沒有':
    if age >=20:
        print('您已經可以考駕照了 可以考慮去報名考駕照')
    else:
        print('沒關係，過幾年您就可以準備考駕照了')
else:
    print('輸入錯誤，請輸入有或沒有')
    
    
