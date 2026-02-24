

#lists1.py
#09.23.25
#N Mazzetti


tempData = []   #Empty list
dayTimeList = ["Mon 9AM","Mon 9PM","Tue 9AM","Tue 9PM","Wed 9AM","Wed 9PM"]   #list of all times of days and days
max = tempData(0)
min = tempData(0)

#make a loop that will take 6 temparture reading

for idx in range (0,6):   #Running this loop 6 times
    v = float(input(dayTimeList[idx]))       #accept value and convert to FLOAT
    tempData.append(v)     #add this number to the list
print(tempData)
t = 0
for idx in range(0,6):

    t = t + tempData[idx]
print(t/6)

for t in range (0,6):
    if (tempData[i] > maxV):


for t in range (0,6):
    if(tempData[i] < minV):

