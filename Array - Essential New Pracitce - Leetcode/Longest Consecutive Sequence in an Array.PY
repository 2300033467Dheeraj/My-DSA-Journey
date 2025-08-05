nums = [100, 4, 200, 1, 3, 2]
nums = sorted(nums)
arr = []
for i in range(0,len(nums)):
    for num in nums:
        if nums[i] + 1  == num:
            arr.append(num)

print(len(arr))