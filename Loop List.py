#lap_time is a list the first time in the list is at postion 0
#the second is potition 1 and third is at position 2
lap_time=[10.98, 12.75, 13.23]

time_to_add=14.75
#Adds to end of list
lap_time.append(time_to_add)
#Changes position 2 to 13.46
lap_time[2]=13.46
#Delete first entry
del lap_time[0]


#Find length of list
list_length=len(lap_time)

#loop from 0 to length of list
for x in range(0,list_length):
    #get value from list depending on the value of x
    time= lap_time[x]
    #Prints time
    print(time)
