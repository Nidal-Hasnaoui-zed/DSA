# we need : An array with values to sort.
l = [7,6,5,4,3,2,1]
n=len(l)
#An outer loop that picks a value to be sorted. 
for i in range(1,n): 
    insert_index = i 
    current_value = l.pop(i)
    for j in range(i-1,-1,-1): 
        if l[j] > current_value : 
            insert_index = j 
    l.insert(insert_index,current_value)
print(f'the sorted array is this one homme {l}')
        
    
