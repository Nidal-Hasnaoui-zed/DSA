# found min value !

my_array = [4,3,2,1] 
min_val = my_array[0]
for i in my_array : 
    if i < min_val : 
        min_val = my_array[i]

print(f'the min value is {min_val}')