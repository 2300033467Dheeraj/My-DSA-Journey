nums = [7, 0, 0, 1, 7, 7, 2, 7, 7]
count = 0
for num in nums:
    if num in nums:
        count += 1
        if count >= len(nums)/2:
            print(num)
            break