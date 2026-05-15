nums = [4,2,5,3,45,34,34,45,724,367,724]
sort = sorted(nums)
unique = []

for i in range(len(nums)):
    if i == 0 or nums[i] !=nums[i-1]:
        unique.append(nums[i])
print(unique)