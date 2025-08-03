# we will learn the selection sort algo in this momrnt !
l = [4,3,2,1]
n = len(l)
for i in range(n-1): 
    min_index = i 
    for j in range(i+1, n):
        if l[j] < l[min_index] : 
            min_index = j 
    min_value = l.pop(min_index)
    l.insert(i,min_value)

print(f'the soreted arrays is this one {l}')            