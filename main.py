#random number generation 
from math import log10
seed=1000
def rannum(seed):
    x=-log10((seed+1)/65536)
    seed= (25173 * seed + 13849) % 65536
    return x
#define the event class, which is the node of the linked list 
class Event():
    def __init__(self, typeofevent=None,  clock=0,numberofstop=None,numberofbus=None):
         
        self.typeofevent = typeofevent
        self.nextevent = None
        self.clock=clock
        self.numberofstop=numberofstop
        self.numberofbus=numberofbus
        
    def whichevent(self):
        return self.typeofevent
    
    def whichbus(self):
        return self.numberofbus
    
    def whichstop(self):
        return self.numberofstop
    
    def whatclock(self):
        return self.clock

#define the event list class, which is the linked list      
class Eventlist():
    def __init__(self):
        self.First_event=Event()
        self.First_event.clock=0        
        self.cur_event=self.First_event
         
    def add_event(self,event):
        self.cur_event.nextevent=event
        self.cur_event=event
    def grow(self,event,newborn):
        
        pre_event=event
        now_event=event.nextevent
        if(now_event):
            
            while(now_event.clock<newborn.clock):
                pre_event=now_event
                now_event=now_event.nextevent
                if(now_event==None):
                    pre_event.nextevent=newborn
                    newborn.nextevent=now_event
                    break
        if(now_event):
            while(now_event.clock==newborn.clock and now_event.typeofevent>newborn.typeofevent):
                pre_event=now_event
                now_event=now_event.nextevent
                if(now_event==None):
                    break
        pre_event.nextevent=newborn
        newborn.nextevent=now_event    
               

#initialization on simulation parameters        
num_of_bus=5
num_of_stop=15
driving_time=300
mean_arrival_rate=2/60
mean_interarrival_rate=1/mean_arrival_rate
boarding_time=3

clock=0
hour=0.1 #set the time length you want to simulate, hour is the unit. 
simulation_time=3600*0.1

#set the priority and representing code of three events 
person=3
boarder=2
arrival=1

# build the initial event list
# the event code: integer value 1 represents "person" event; 2:"arrival"event ; 3:"boarder"event

eventlist= Eventlist()

#initialize the person event 
for i in range(0,num_of_stop):   
    a=Event(typeofevent=person,clock=0,numberofstop=i)
    eventlist.add_event(a)

#initialize the queue at each stop 
ppl_at_stop=[]
for x in range(0,num_of_stop):
    ppl_at_stop.append(0)

#initialize the arrival event 
for i in range(0,num_of_bus):
    a=Event(typeofevent=arrival,clock=0,numberofbus=i,numberofstop=i*3)
    eventlist.add_event(a)



#main loop 
event=eventlist.First_event
while clock<=simulation_time:
    
    clock=event.clock
    whichevent=event.typeofevent
    whichbus=event.numberofbus
    whichstop=event.numberofstop
    rightnow_event=event
    
    #person 
    if whichevent==person:
        print("person")
        ppl_at_stop[whichstop]+=1
        newborn=Event(typeofevent=person,clock=clock+mean_interarrival_rate*rannum(seed),numberofstop=whichstop)
        eventlist.grow(event=event,newborn=newborn)
    #arrival   
    elif whichevent==arrival:
        print("arrival")
        if ppl_at_stop[whichstop]==0:
            newborn=Event(typeofevent=arrival,clock=clock+driving_time,numberofbus=whichbus,numberofstop=whichstop+1)
            eventlist.grow(event=event,newborn=newborn)
            
        else:
            
            newborn=Event(typeofevent=boarder,clock=clock,numberofstop=whichstop)
            eventlist.grow(event=event,newborn=newborn)
    #boarder   
    elif whichevent==boarder:
        print("boarder")
        ppl_at_stop[whichstop]-=1
        if ppl_at_stop[whichstop]==0:
            newborn=Event(typeofevent=arrival,clock=clock+driving_time,numberofbus=whichbus,numberofstop=whichstop+1)
            eventlist.grow(event=event,newborn=newborn)
        else:
            newborn=Event(typeofevent=boarder, clock=clock+boarding_time,numberofstop=whichstop)
            eventlist.grow(event=event,newborn=newborn)
    else:
        pass 
    
    event=event.nextevent

print(ppl_at_stop)
print("The simulation is over now.")
        
    
    
    



    






    