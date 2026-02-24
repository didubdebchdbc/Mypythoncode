#N Mazzetti
#22.10.25
#hwordsort

#Enter the words you want with different amount of letters but all start with the letter H


array = ["however", "Helmet", "Hospital", "Highway", "high", "Hunger", "Hi", "Habit", "Humble", "Highlight"]
size = len(array)
pass_=0
# Make an outer loop to go through the whole array

for i in range(0,size):
    #make an inner loop that goes from 0 until len-1.
    for j in range(0, size-i-1):
        if(len(array[j])>len(array[j+1])):
            #swap these values
            array[j], array[j+1], array[j]
            #the remaining arrays.
    pass_=pass_+1
    print("After pass", pass_)
    print(array)
#outside the loops print the array
print(array)
