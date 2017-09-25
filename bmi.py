#!/usr/bin/env python3
# -*- coding: utf-8 -*-

weight = int(input('Input your weight: '))
height = int(input('Input your height: ')) / 100
bmi = weight / (height * height)
print('Your BMI is %.2f' % bmi)
if bmi > 32:
    print('严重肥胖')
elif bmi > 28:
    print('肥胖')
elif bmi > 25:
    print('过重')
elif bmi >= 18.5:
    print('正常')
else:
    print('过轻')
