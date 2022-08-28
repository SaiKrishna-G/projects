# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 14:14:19 2022

@author: gsaik
"""


import matplotlib.pyplot as plt
from matplotlib.patches import Arc


def PlotPitch():
    
    
    #Create figure
    #Create figure
    fig=plt.figure(facecolor=('mediumseagreen'))
    ax=fig.add_subplot(1,1,1)
    #Pitch Outline & Centre Line
    plt.plot([0,0],[0,80], color="white")
    plt.plot([0,120],[80,80], color="white")
    plt.plot([120,120],[80,0], color="white")
    plt.plot([120,0],[0,0], color="white")
    plt.plot([60,60],[0,80], color="white")
    
    #Left Penalty Area
    plt.plot([0,18],[18,18],color="white")
    plt.plot([18,18],[18,62],color="white")
    plt.plot([18,0],[62,62],color="white")
    
    #Right Penalty Area
    plt.plot([120,102],[18,18],color="white")
    plt.plot([102,102],[18,62],color="white")
    plt.plot([102,120],[62,62],color="white")
    
    #Left 6-yard Box
    plt.plot([0,6],[30,30],color="white")
    plt.plot([6,6],[30,50],color="white")
    plt.plot([6,0],[50,50],color="white")
    
    #Right 6-yard Box
    plt.plot([120,114],[50,50],color="white")
    plt.plot([114,114],[50,30],color="white")
    plt.plot([114,120],[30,30],color="white")
    
    #left goalposts
    plt.plot([-2,0],[36,36],color="white")
    plt.plot([0,0],[36,44],color="white")
    plt.plot([0,-2],[44,44],color="white")
    plt.plot([-2,-2],[44,36],color="white")
    
    #right goal posts
    plt.plot([120,122],[36,36],color="white")
    plt.plot([122,122],[36,44],color="white")
    plt.plot([122,120],[44,44],color="white")
    plt.plot([120,120],[44,36],color="white")
   
    #Prepare Circles
    centreCircle = plt.Circle((60,40),10,color="white",fill=False)
    centreSpot = plt.Circle((60,40),1,color="white")
    leftPenSpot = plt.Circle((12,40),1,color="white")
    rightPenSpot = plt.Circle((108,40),1,color="white")
    
    #Draw Circles
    ax.add_patch(centreCircle)
    ax.add_patch(centreSpot)
    ax.add_patch(leftPenSpot)
    ax.add_patch(rightPenSpot)
    
    #Prepare Arcs
    leftArc = Arc((12,40),height=20,width=20,angle=0,theta1=310,theta2=50,color="white")
    rightArc = Arc((108,40),height=20,width=20,angle=0,theta1=130,theta2=230,color="white")
    
   
    
    #Draw Arcs
    ax.add_patch(leftArc)
    ax.add_patch(rightArc)
    
   
            
    #Remove Axes
    plt.axis('off')
    return (fig,ax)

