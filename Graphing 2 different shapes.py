# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 13:32:28 2020

@author: matt hanson
"""

import math
import matplotlib.pyplot as plt

#put e or E for type of graph for a epitrochoid
#put h or H for type of graph for a hypotrochoid
def spiral(R,r,d,type_of_graph):
    def epit(R, r, d):
        x=[]
        y=[]
        N=R*r/math.gcd(R,r)
        N=N/R
        for num in range(50000):
            theta=num*math.pi*2*N
            theta=theta/50000
            x.append((r+R)*math.cos(theta) + -d*math.cos(((r+R)/r)*theta))
            y.append((r+R)*math.sin(theta) + -d*math.sin(((r+R)/r)*theta))
        return(x,y)
    def hypo(R, r, d):
        x1=[]
        y1=[]
        N=R*r/math.gcd(R,r)
        N=N/R
        for num in range(50000):
            theta=num*math.pi*2*N
            theta=theta/50000
            x1.append((r-R)*math.cos(theta) + d*math.cos(((r-R)/r)*theta))
            y1.append((r-R)*math.sin(theta) + -d*math.sin(((r-R)/r)*theta))
        return(x1,y1)
    if type_of_graph=='E' or type_of_graph=='e':
        x,y=epit(R,r,d)
    if type_of_graph=='H' or type_of_graph=='h':
        x,y=hypo(R,r,d)
    return x,y




#plot 1 for an epitrochoid
plt.figure(figsize=(8,8))
plt.subplot(2,2,1)
for num in range(27):
    x11,y11=spiral(20+num,1,17, 'e')
    plt.plot(x11,y11,antialiased=True,clip_on=False)
plt.xlabel('x(Θ)')
plt.ylabel('y(Θ)')
plt.title('Epitrochoid Graph: Jawbreaker')



#plot 2 for a hypotrochoid
plt.subplot(2,2,2)
for num in range(100):
    x2,y2=spiral(35,75,28+num,'H')
    plt.plot(x2,y2,antialiased=True,clip_on=False)
plt.xlabel('x(Θ)')
plt.ylabel('y(Θ)')
plt.title('Hypotrochoid Graph: Mind Control')

#plot 3 for a epitrochoid
plt.subplot(2,2,3)
for num in range(1,25):
    x33,y33=spiral(75,num,35+num,'e')
    if num%2==0:
        plt.plot(x33,y33,'r',antialiased=True,clip_on=False)
    else:
        plt.plot(x33,y33,'aqua',antialiased=True,clip_on=False)
for num in range(8):
    x33,y33=spiral(2+num,1,0,'e')
    plt.plot(x33,y33,'k',antialiased=True,clip_on=False) 
for num in range(25):
    x33,y33=spiral(7+num,1,0,'e')
    plt.plot(x33,y33,'cornflowerblue',antialiased=True,clip_on=False)
plt.xlabel('x(Θ)')
plt.ylabel('y(Θ)')
plt.title('Epitrochoid Graph: Red Eye')

#plot 4 for a hyptrochoid
plt.subplot(2,2,4)
for num in range(27,31):
    x44,y44=spiral(10+num,120,156,'H')
    plt.plot(x44,y44,antialiased=True,clip_on=False)
plt.xlabel('x(Θ)')
plt.ylabel('y(Θ)')
plt.title('Hypotrochoid Graph: The Pentagram')
plt.tight_layout()
#plt.savefig('project1final1figure.pdf')