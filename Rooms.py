room=0
rooms=[0,1,2,3,4,5,6,7,8,9,10,11,12]
winrooms=[12]
lossrooms=[4,10,11]
winflag=0
loseflag=0
roomsummary=["You are in the Garden. Darkness everywhere.","You are in the Bathroom. You hear a sound.","You are in the Hall. You almost tripped. Stairway East.","You are in the Storage. The atmosphere is suffocating. Stairway West, Pathway South.","You made it to the Living room. You found you're Father.","You are in the Salon. There is the sound of music.","You are in the Dinning room. Everything is a mess.","You are in the Hallway. It's Dark. Stairway South","You are in the Kitchen. You hear voices.","You are in the Upper hallway. Silence everywhere.","You are in you're Brother's room. Your Brother is telling on you.","You are in you're Parent's room. Your Mother caught you.","You are in you're room. You are safe."]
Pdirections=[{1:2},{2:2},{0:0,1:5,2:3,3:1},{1:8,3:2},{1:6,2:5},{0:2,1:8,3:4},{0:4,1:7},{0:6,1:9,2:8},{0:5,2:3,3:7},{0:7,1:11,2:12,3:10},{2:9},{0:9},{3:9}]
directions=["South","East","North, South, East or West","South or West","South or East","North, South or West","North or South","North, South or East","North, East or West","North, South, East or West","East","North","West"]
print ("You have Sneaked out of your home at night. Go to your room without getting spotted!")
print ("Chose direction to go.(Tip: 0 is North, 1 is South, 2 is East, 3 is West)")
while (loseflag==0 and winflag==0):
    print (roomsummary[room])
    if (room in winrooms):
        winflag=1
    if (room in lossrooms):
        loseflag=1
    if (loseflag==0 and winflag==0):
        print (directions[room])
        x=int(input("Give direction:"))
        while ((x>3 or x<0) or (x not in Pdirections[room])):
            x=int(input("Give valid direction:"))
        room=Pdirections[room][x]
if (winflag==1):
    print ("Congatulations!!! You have made it to your room!!!")
else:
    print ("Game over. You have been caught...")
    
