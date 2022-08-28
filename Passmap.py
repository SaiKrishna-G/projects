# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 11:04:22 2022

@author: gsaik
"""

import json
import matplotlib.pyplot as plt

from matplotlib.patches import Arc


 
#load competititons 

f= open('C:\\Users\\gsaik\\Downloads\\statsbomb data\\data\\competitions.json')
competitions =json.load(f)

competition_id =53

#load matches

f=open('C:\\Users\\gsaik\\Downloads\\statsbomb data\\data\\matches\\'+str(competition_id)+'\\106.json',encoding ='utf-8')
matches =json.load(f)


# obtain the required match id

home_team_required="England Women's"
away_teamrequired="Germany Women's"

for match in matches:
     home_teamname=match['home_team']['home_team_name']
     away_teamname=match['away_team']['away_team_name']
     if(home_team_required==home_teamname) and (away_teamrequired==away_teamname):
        match_id_required=match['match_id']

print("The ID of match "+home_team_required+" vs "+away_teamrequired+" is : "+ str(match_id_required))

#load that match event data

data_file= open('C:\\Users\gsaik\Downloads\statsbomb data\data\events\\'+str(match_id_required)+'.json')
    
data = json.load(data_file)


from pandas.io.json import json_normalize
df = json_normalize(data, sep = "_").assign(match_id = match_id_required)

#creating dataframe of passes

passes = df.loc[df['type_name'] == 'Pass'].set_index('id')

#plot pitch


length=120
width=80


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
    #Display Pitch


(fig,ax)=PlotPitch()

for i,thepass in passes.iterrows():
 
    if thepass['player_name']=='Keira Walsh':
        x=thepass['location'][0]
        y=thepass['location'][1]
        passCircle=plt.Circle((x,width-y),2,color="blue")      
        passCircle.set_alpha(.2)   
        ax.add_patch(passCircle)
        dx=thepass['pass_end_location'][0]-x
        dy=thepass['pass_end_location'][1]-y

        passArrow=plt.Arrow(x,width-y,dx,-dy,width=3,color="blue")
        ax.add_patch(passArrow)
        
plt.title("PASS MAP OF KEIRA WALSH -EURO 2O22 FINAL")        
plt.show()        
