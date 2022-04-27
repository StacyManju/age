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
    
