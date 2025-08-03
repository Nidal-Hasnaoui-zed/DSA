# here i will learn the bubbl sort algorithmes : 


# creating an array : 
my_array = [4,3,2,1]
n = len(my_array)
for i in range(n-1): 
    for j in range(n-i-1): 
        if my_array[j] > my_array[j+1] :
            my_array[j] , my_array[j+1] = my_array[j+1] , my_array[j]
            swapped = True 
        if not swapped : 
            break 
print(f'The sorted array is {my_array}')
            
# for understtand the consepts of loops we have this one : 
        # outer loop !
#  our array : [4,3,2,1]
# for we can sorte it we have this one bro : 
# case 1 : [3,2,1,4]
# case 2 : [2,1,3,4]
# case 3 : [1,2,3,4]
# len(array) = 4 
# and for we can sorted we mut loop jut 3 times 
# and this is the demonstrantion of why we use n-1 in outer loop !

    # inner loop !

#lets take our simplw array : 
# our arrays is  [4,3,2,1]
# the condition of innner loop is n-i-1 : 
# case  1 : i = 0 and n=4 so inner loop go from 0 to 3 : 
# it loop 3 times in case 1 that force 4 go to last of array ! [3,2,1,4]
#case 2 : i=1 and n 0 4 so inner loop go from 0 to 2 : 
#it loop 2 times in case 2 that force 3 go to his correct position [2,1,3,4]
# and this is the demonstration iìif why we use n-i-1 in inner loop !
