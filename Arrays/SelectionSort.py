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

# the outer loop is control how much time inner loop must run !
# the putput of this one len(my_array) = 4
# case 1 : [1,4,3,2]
# case 2 : [1,2,4,3]
# case 3 : [1,2,3,4]
# as you see for you can sort this array you need loop just 3 times bro so outer loop go into n-1 

# lets talk right kenw about the inner loop !



