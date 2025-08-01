# okey i understand this bro : 
my_array = [4,3,2,1]
n= len(my_array)
for i in range(n-1): 
    min_index = i 
    for j in range(i+1, n): 
        if my_array[j] < my_array[min_index] : 
            min_index = j 
    # this take alot of values bro !
    # min_value = my_array.pop(min_index)
    # my_array.insert(i,min_value)
    
    
    # iwill show you the best one bro hahahah !

print(f'the sorted array is readu {my_array}')

# the outer loop is control how much time inner loop must run !
# the putput of this one len(my_array) = 4
# case 1 : [1,4,3,2]
# case 2 : [1,2,4,3]
# case 3 : [1,2,3,4]
# as you see for you can sort this array you need loop just 3 times bro so outer loop go into n-1 

# lets talk right kenw about the inner loop !
# after we do a varable min_index take the first index in insorted array : 
# in our case i = 0 so min_index is 0 
#after we create a inner loop do this one bro !
#the inner loop go from i+1 into last of array and cosider the i is the min index !
#after we do an condition if we found other value in our array is less than the min index we  put it inside the min_index and this is the rull of inner loop !
# after we take this min value we found and we pop it from his place and put it in the i index !




