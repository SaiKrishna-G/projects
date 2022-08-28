# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 12:05:43 2022

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

#print all matches results

for match in matches:
    home_teamname=match['home_team']['home_team_name']
    away_teamname=match['away_team']['away_team_name']
    home_team_score=match['home_score']
    away_team_score=match['away_score']
    print ("The match between "+home_teamname+" and "+away_teamname+" finished "+str(home_team_score)+" : "+str(away_team_score))

#obtain all england matches
   

team_required="England Women's"

for match in matches:
    home_teamname=match['home_team']['home_team_name']
    away_teamname=match['away_team']['away_team_name']
    home_team_score=match['home_score']
    away_team_score=match['away_score']
    if((team_required==home_teamname) or (team_required==away_teamname)):
        
        
      print ("The match between "+home_teamname+" and "+away_teamname+" finished "+str(home_team_score)+" : "+str(away_team_score))

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

#A dataframe of shots
    
shots = df.loc[df['type_name'] == 'Shot'].set_index('id')

#plot a pitch


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

#SHOT MAP 

#plot the shots on pitch



for i,shot in shots.iterrows():
    x=(shot['location'][0])
    y=(shot['location'][1])    
    goal=shot['shot_outcome_name']=='Goal'
    team_name=shot['team_name']
 
    circleSize=2
 
    if (team_name==home_team_required):
        if goal:
            shotCircle=plt.Circle((x,width-y),circleSize,color="red")
            plt.text((x+1),width-y+1,shot['player_name']) 
        else:
            shotCircle=plt.Circle((x,width-y),circleSize/2,color="red")     
            shotCircle.set_alpha(.2)
    elif (team_name==away_teamrequired):
        if goal:
            shotCircle=plt.Circle((length-x,y),circleSize,color="blue") 
            plt.text((length-x+1),y+1,shot['player_name']) 
        else:
            shotCircle=plt.Circle((length-x,y),circleSize/2,color="blue")      
            shotCircle.set_alpha(.2)
    ax.add_patch(shotCircle)
  #reduced the size of shots which didn't result in goals to
  #just avoid overlapping
  
    
plt.text(5,75,away_teamrequired + ' shots') 
plt.text(70,75,home_team_required + ' shots') 

plt.title("SHOT MAP OF WOMENS EUROS 2022 FINAL")     
plt.show()


#FOR XG MAP USE THIS CODE
"""
    circleSize=(shot['shot_statsbomb_xg'])*1
 
    if (team_name==home_team_required):
        if goal:
            shotCircle=plt.Circle((x,width-y),circleSize,color="red")
            plt.text((x+1),width-y+1,shot['player_name']) 
        else:
            shotCircle=plt.Circle((x,width-y),circleSize,color="red")     
          
    elif (team_name==away_teamrequired):
        if goal:
            shotCircle=plt.Circle((length-x,y),circleSize,color="blue") 
            plt.text((length-x+1),y+1,shot['player_name']) 
        else:
            shotCircle=plt.Circle((length-x,y),circleSize,color="blue")      
           
    ax.add_patch(shotCircle)
  #reduced the size of shots which didn't result in goals to
  #just avoid overlapping
  
    
plt.text(5,75,away_teamrequired + ' shots') 
plt.text(70,75,home_team_required + ' shots') 
plt.title("XG MAP OF WOMENS EUROS 2022 FINAL")     
     
plt.show()
"""