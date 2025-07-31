nums = [2, 3, 5, -2, 7, -4]
count = 0
total = []
for i in range(len(nums)):
    count += nums[i]
    total.append(count)
print(max(total))