# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 13:59:34 2024

@author: OPS
"""
temperature = float(input('Enter Temperature: '))
print(temperature)
if temperature < 30:
    print('It is a cold day')
    print('keep worm and drink coffee')
elif temperature >= 40 and temperature <= 50:
    print ('it is a nice day')
elif temperature > 50:
    print('it is a worm day')
    print('drink maximum water')
print('done')





