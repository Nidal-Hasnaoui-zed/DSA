my_array = [4,3,2,1]
min_val = my_array[0]
n = len(my_array)
for i in range(n) : 
    if my_array[i] < min_val : 
        min_val = my_array[i]
print(f'min val is {min_val}') 
            