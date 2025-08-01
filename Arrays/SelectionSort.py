# okey i understand this bro : 
my_array = [4,3,2,1]
n= len(my_array)
for i in range(n-1): 
    min_index = i 
    for j in range(i+1, n): 
        if my_array[j] < my_array[min_index] : 
            min_index = j 
    min_value = my_array.pop(min_index)
    my_array.insert(i,min_value)

print(f'the sorted array is readu {my_array}')
