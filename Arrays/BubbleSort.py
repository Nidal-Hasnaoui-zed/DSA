# here i will learn the bubbl sort algorithmes : 


# creating an array : 
my_array = [7,12,9,11,3]
n = len(my_array)
for i in range(n-1): 
    for j in range(n-i-1): 
       if my_array[j] > my_array[j+1] : 
           my_array[j], my_array[j+1] = my_array[j+1] ,my_array[j]
           
print(F'the sorted array is : {my_array}')

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

    # outer loop !


