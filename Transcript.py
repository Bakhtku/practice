# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 16:10:54 2024

@author: OPS
"""

name= input ('Enter your name please ')
print(f"Hello {name} ")
physics = float(input('enter marks obtained in physics '))
chemistry = float(input('entermarks obtained in Chemistry '))
maths = float(input('enter marks secured in maths '))
bio = float(input('enter marks secured in Bio '))
cs = float(input('enter marks secured in Computer Science '))
marks = physics + chemistry + maths + bio + cs
print (marks)
percentage = marks * 100 / 500
print (float(percentage))
if percentage > 100:
    print("Sorry you have enterred wrong numbers, Enter correct numbers")    
elif percentage >= 90 and percentage <100:
    print("Congratualations you have passed the test")
    print ("Grade = A+")
elif percentage >= 80:
        print("Congratualations you have passed the test")
        print ("Grade = A")
elif percentage >= 70:
    print("Congratualations you have passed the test")
    print ("Grade = B")
elif percentage >=60:
    print(f"Congratualations {name} you have passed the test")
    print ("Grade = C")
else: 
    print(f"sorry {name} you could not pass the test, better luck next time")
print ('done')
