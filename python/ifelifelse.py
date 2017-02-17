# -*- coding: utf-8 -*-

height = 1.75
weight = 80.5

bmi = weight / (height * height)
if bmi < 18.5:
    print('过轻')
elif bmi < 25:
    print('正常')
elif bmi < 28:
    print('过重')
elif bmi < 32:
    print('肥胖')
else :
    print('严重肥胖')

height = float(input('输入体重（kg）: '))
weight = float(input('输入身高（m）: '))

bmi = weight / (height * height)
if bmi < 18.5:
    print('过轻')
elif bmi < 25:
    print('正常')
elif bmi < 28:
    print('过重')
elif bmi < 32:
    print('肥胖')
else :
    print('严重肥胖')
