
# Bubble sort
# N Mazzetti
# 21.10.25

#Enter which numbers do you want to
array = [79,10,92,103,96,3,193,120]
size = len(array)
pass_=0
# Make an outer loop to go through the whole array

for i in range(0,size):
    #make an inner loop that goes from 0 until len-1.
    for j in range(0, size-i-1):
        if(array[j]>array[j+1]):
            #swap these values
            array[j], array[j+1], array[j]
            #the remaining arrays.
    pass_=pass_+1
    print("After pass", pass_)
    print(array)
#outside the loops print the array
print(array)





