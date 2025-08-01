# Bubble sort alogorihtme !

my_array = [4,3,2,1] 
n = len(my_array)
for i in range(n-1): 
    for j in range(n-i-1): 
        if my_array[j] > my_array [j+1] : 
            my_array[j] , my_array [j+1] = my_array[j+1] , my_array[j]
            
print(f'the sorted array is {my_array}')