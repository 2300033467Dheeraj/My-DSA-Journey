nums = [1, 6, 2, 10, 3]
target = 7
number = 0 
for i in range(len(nums)):
    for j in range(1,len(nums)):
        
        if  nums[i] + nums[j] == target :
            print(i,j)
