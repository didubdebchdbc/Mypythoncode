
#N Mazzetti
#12.11.25
#Binary search

import random

Array = []
for i in range(1000):
   Array.append(random.randint(1,1000))

Array.sort()
T = 345

Low = 0
High = len(Array)
Mid = (Low+T)//2

while(Low<=High):
    if(Array[Mid]==T):
        print("f")
    if(Array[Mid]<T):
        Low=Mid+1
    if(Array[Mid]>T):
        High=Mid-1
    Mid=(Low+High)//2