# -*- coding: utf-8 -*-
"""
Created on Sun May 28 13:00:52 2017

@author: User
"""
import matplotlib.pyplot as plt
x2=[2,3,4]
y2 =[15,3,6]
plt.plot(x2,y2,label ='second line')
plt.xlabel('plot number')
plt.ylabel('Important var')
plt.title('Interesting graph\ncheck it out')
plt.plot([1,2,3],[5,7,4],label ='First line')
plt.legend()
'''cannot use 3 matrix rows'''  
plt.show()

