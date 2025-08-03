#we will learn the bubblt sore algo : 
l = [4,3,2,1]
n = len(l)
for i in range(n-1): 
    for j in range(n-i-1): 
        if l[j] > l[j+1] : 
            l[j] , l[j+1] = l[j+1] , l[j]

print(f'the sorted array is {l}')