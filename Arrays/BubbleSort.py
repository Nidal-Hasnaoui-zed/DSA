# here i will learn the bubbl sort algorithmes : 


# creating an array : 
my_array = [7,12,9,11,3]
n = len(my_array)
for i in range(0,n): 
    for j in range(i+1,n):
        if my_array[i] > my_array[j]: 
            my_array[i] = my_array[j]